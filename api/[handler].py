import os
import json
import logging
from datetime import datetime


import falcon
import firebase_admin
from firebase_admin import credentials, firestore



log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

base_route: str = "/api"

class FirebaseException(Exception):
    pass

class BaseHandler:
    db = None

    def __init__(self, firebase: bool = False):
        if firebase:
            self.connect_firebase()

    def connect_firebase(self) -> None:
        try:
            creds = json.loads(os.getenv("GOOGLE_AUTH"))
            certificate = credentials.Certificate(creds)
            firebase_admin.initialize_app(certificate, {"projectId": creds['project_id']})
            self.db = firestore.client()

        except Exception as e:
            log.critical(f'{e}')

    def on_get(self, request, response) -> None:
        response.media = {'status': 'OK'}


class MailHandler:
    def on_get(self, request, response) -> None:
        response.media = {"mail": "email"}


class EventsHandler(BaseHandler):
    def on_get(self, request, response) -> None:

        try:
            events_ref = (
                self.db.collection("Events").where("Date", ">=", datetime.now())
                if not request.get_param("old")
                else self.db.collection("Events").where("Date", "<=", datetime.now())
            )

            docs_generator = events_ref.stream()
            documents = []
            for doc in docs_generator:
                doc_dict = doc.to_dict()
                doc_dict["id"] = doc.id
                doc_dict["Date"] = doc_dict["Date"].rfc3339()
                documents.append(doc_dict)

            response.media = {"events": documents}

        except Exception as fbe:
            log.critical(f'{fbe}')
            response.status = 500
            response.media = {'status': 'an error has occurred and has been reported'}


class SingleEventHandler(BaseHandler):
    def on_get(self, request, response) -> None:
        db = firestore.client()

        events_ref = (
            db.collection("Events").where("Date", ">=", datetime.now())
            if not request.get_param("old")
            else db.collection("Events").where("Date", "<=", datetime.now())
        )

app = falcon.App(cors_enable=True)
app.add_route(f"{base_route}/handler", BaseHandler())
app.add_route(f"{base_route}/mail", MailHandler())
app.add_route(f"{base_route}/events", EventsHandler(True))
app.add_route(f"{base_route}/events/{{id}}", EventsHandler())
