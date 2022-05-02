import falcon
import os
import firebase_admin
from firebase_admin import credentials, firestore
import json

try:
    cred = credentials.Certificate(json.loads(os.getenv("GOOGLE_AUTH")))
    f = firebase_admin.initialize_app(cred, {
        'projectId': "sveltechi-dev" })
except Exception as e:
    print(f'{e}')
    exit()


base_route: str = "/api"

class BaseHandler:
    def on_get(self, request, response) -> None:
        response.media = {'hello': 'world'}


class MailHandler:
    def on_get(self, request, response) -> None:
        response.media = {'mail': 'email'}

class EventHandler:
    def on_get(self, request, response) -> None:
        db = firestore.client()
        events_ref = db.collection(u'Events')
        docs_generator = events_ref.stream()
        d = []
        for doc in docs_generator:
            doc_dict = doc.to_dict()
            d.append(doc_dict)

        response.media = {'events': str(d)}


app = falcon.App(cors_enable=True)
app.add_route(f'{base_route}/handler', BaseHandler())
app.add_route(f'{base_route}/mail', MailHandler())
app.add_route(f'{base_route}/events', EventHandler())