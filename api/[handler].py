import falcon
import os
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import json

try:
    creds = json.loads(os.getenv("GOOGLE_AUTH"))
    certificate = credentials.Certificate(creds)
    f = firebase_admin.initialize_app(certificate, {"projectId": creds['project_id']})
except Exception as e:
    print(f"{e}")
    # exit()


base_route: str = "/api"


class BaseHandler:
    def on_get(self, request, response) -> None:
        response.media = {"hello": "world"}


class MailHandler:
    def on_get(self, request, response) -> None:
        response.media = {"mail": "email"}


class EventsHandler:
    def on_get(self, request, response) -> None:
        db = firestore.client()

        events_ref = (
            db.collection("Events").where("Date", ">=", datetime.now())
            if not request.get_param("old")
            else db.collection("Events").where("Date", "<=", datetime.now())
        )

        docs_generator = events_ref.stream()
        documents = []
        for doc in docs_generator:
            doc_dict = doc.to_dict()
            doc_dict["id"] = doc.id
            doc_dict["Date"] = doc_dict["Date"].rfc3339()
            documents.append(doc_dict)

        response.media = {"events": documents}


class SingleEventHandler:
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
app.add_route(f"{base_route}/events", EventsHandler())
app.add_route(f"{base_route}/events/{{id}}", EventsHandler())
