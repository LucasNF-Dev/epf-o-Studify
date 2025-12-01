import os

class Config:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    HOST = 'localhost'
    PORT = 8080
    DEBUG = True
    RELOADER = True

    TEMPLATE_PATH = os.path.join(BASE_DIR, 'views')
    STATIC_PATH = os.path.join(BASE_DIR, 'static')
    DATA_PATH = os.path.join(BASE_DIR, 'data')

    SECRET_KEY = 'sua-chave-secreta-aqui'
