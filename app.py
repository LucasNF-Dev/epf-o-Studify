from bottle import Bottle, static_file, redirect
from database import create_tables
from controllers.flashcard_controller import flashcard_routes
from controllers.user_controller import user_routes

def create_app():
    create_tables()

    app = Bottle()

    @app.route('/')
    def home():
        return redirect('/users')

    @app.route('/static/<filepath:path>')
    def server_static(filepath):
        return static_file(filepath, root='static')

    app.mount("/flashcards", flashcard_routes)
    app.mount("/users", user_routes)

    return app
