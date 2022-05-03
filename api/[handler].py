import falcon
import os
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import json

try:
    # handle local envvar while vercel is broken
    creds_env = os.getenv("GA") if os.getenv("GA") else os.getenv("GOOGLE_AUTH")
    cred = credentials.Certificate(json.loads(creds_env))
    f = firebase_admin.initialize_app(cred, {"projectId": "sveltechi-dev"})
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


class EventHandler:
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
            doc_dict["Date"] = doc_dict["Date"].rfc3339()
            documents.append(doc_dict)

        response.media = {"events": documents}


app = falcon.App(cors_enable=True)
app.add_route(f"{base_route}/handler", BaseHandler())
app.add_route(f"{base_route}/mail", MailHandler())
app.add_route(f"{base_route}/events", EventHandler())
