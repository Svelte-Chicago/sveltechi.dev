import os
import json
import logging
from typing import Optional
from datetime import datetime
import falcon
import firebase_admin
from firebase_admin import credentials, firestore


console_out = logging.StreamHandler()
console_out.setLevel(logging.DEBUG)
logging.getLogger(__name__).addHandler(console_out)
logging.debug("BEGINNING STARTUP")
try:
    google_credentials= json.loads(os.getenv("GOOGLE_AUTH"))
except json.decoder.JSONDecodeError as jde:
    logging.critical(f'{jde}')
    exit()
logging.debug('STARTUP COMPLETE')


base_route: str = "/api"
cache_timeout: int = int(os.getenv('CACHE_TIMEOUT', 120)) # default cache timeout 2mins


class APIException(falcon.HTTPInternalServerError):
    pass

class BaseHandler:
    """Fondational class that may or may not attempt to connect to firebase

    Attributes:
        db
    """
    db: Optional[firestore.Client] = None
    credentials: Optional[dict] = False
    fba = False

    def __init__(self, firebase: bool = False, google_creds: Optional[dict] = False):
        if firebase:
            self.credentials = google_creds
            self.connect_firebase()

    def connect_firebase(self) -> None:
        try:
            logging.debug(f"Connecting to firebase project {self.credentials['project_id']}...")
            # print(self.credentials)
            certificate = credentials.Certificate(self.credentials)
            if not self.fba:
                firebase_admin.initialize_app(certificate, {"projectId": os.getenv("FIREBASE_PROJECT")})
            self.db = firestore.client()
        except Exception as e:
            logging.critical(f'{e}')

    def on_get(self, request, response) -> None:
        response.media = {'status': 'OK'}


class MailHandler:
    '''Supports the event confirmation process for event RSVPs
    '''
    def on_get(self, request, response) -> None:
        response.media = {"mail": "email"}


class EventsHandler(BaseHandler):
    '''Gets a list of events from firestore

    '''

    cache = {
        'age': 0,
        'documents': []
    }

    def on_get(self, request, response, **params) -> None:


        if 'id' not in params.keys():
            logging.debug("GETTING EVENTS")

            documents = self.get_documents()
            events = []
            if request.get_param('old'):
                events = [doc for doc in documents if int(doc['Date']) < int(datetime.now().timestamp()) ]
            else:
                events = [doc for doc in documents if int(doc['Date']) > int(datetime.now().timestamp()) ]
            response.append_header('cache-control', 's-maxage=10, stale-while-revalidate')
            response.media = {'events': events }
        else:
            logging.debug(f"GETTING SINGLE EVENT {params['id']}")
            response.append_header('cache-control', 's-maxage=10, stale-while-revalidate')
            response.media = self.get_single_document(params['id'])

    def get_documents(self) -> list:

        documents = []

        if not self.db:
            self.connect_firebase()

        if self.cache['age'] < int(datetime.now().timestamp()) - cache_timeout or len(self.cache['documents']) == 0:
            logging.debug("CACHE OUT OF DATE OR EMPTY")
            try:
                events_ref = self.db.collection("Events")

                docs_generator = events_ref.stream()
                for doc in docs_generator:
                    doc_dict = doc.to_dict()
                    doc_dict["id"] = doc.id
                    doc_dict["Date"] = doc_dict["Date"].timestamp()
                    documents.append(doc_dict)

                # replace our cache
                self.cache = {
                    'age': int(datetime.now().timestamp()),
                    'documents': documents
                }

            except Exception as fbe:
                logging.critical(f'{fbe}')
                raise APIException(description='Events could not be retrieved. This error has been noted')
        else:
            documents = self.cache['documents']

        return documents


    def get_single_document(self, id):
        documents = self.get_documents()

        doc_reduction = [doc for doc in documents if doc['id'] == id]

        if len(doc_reduction) == 0:
            raise falcon.HTTPNotFound
        elif len(doc_reduction) > 1:
            raise falcon.HTTPNotFound(description="document id was ambiguous")
        else:
            return doc_reduction[-1]


app = falcon.App(cors_enable=True)
eh = EventsHandler(True, google_credentials)

app.add_route(f"{base_route}/handler", BaseHandler())
app.add_route(f"{base_route}/mail", MailHandler())
app.add_route(f"{base_route}/event/{{id}}", eh)
app.add_route(f"{base_route}/events", eh)
