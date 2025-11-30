# main.py
from app import create_app
from bottle import run
from beaker.middleware import SessionMiddleware
import os

if __name__ == '__main__':
    app = create_app()
    session_opts = {
        'session.type': 'file',
        'session.cookie_expires': 3600,      # 1 hora
        'session.data_dir': './sessions',    # pasta onde as sessões serão salvas
        'session.auto': True
    }
    os.makedirs(session_opts['session.data_dir'], exist_ok=True)
    app = SessionMiddleware(app, session_opts)
    run(app=app, host="localhost", port=8080, debug=True, reloader=True)
