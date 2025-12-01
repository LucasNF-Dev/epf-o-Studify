# home_controller.py

from bottle import Bottle, request, template, redirect
from config import Config
from .base_controller import BaseController # NOVO: Importe BaseController se não estiver lá

class HomeController(BaseController): # NOVO: Herde de BaseController para ter 'render' e 'redirect'
    def __init__(self, app):
        super().__init__(app) # NOVO: Chame o construtor do pai
        # Não precisa mais de self.app = app
        self.setup_routes()

    def setup_routes(self):
        # Apenas a rota pública /
        self.app.route('/', method='GET', callback=self.home_public)
        # self.app.route('/studify', method='GET', callback=self.home_private) # <-- REMOVIDO!
    
    def home_public(self):
        # Página inicial independente de login
        return self.render('home_public') # NOVO: Use self.render do BaseController

    # A função home_private foi removida/substituída pela lógica de studify.py