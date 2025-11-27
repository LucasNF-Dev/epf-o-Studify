from bottle import Bottle
from database import create_tables

from controllers.flashcard_controller import flashcard_routes
from controllers.user_controller import user_routes

def create_app():
    create_tables()

    app = Bottle()

    app.mount("/flashcards", flashcard_routes)
    app.mount("/users", user_routes)

    return app
