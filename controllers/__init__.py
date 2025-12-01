# controllers/__init__.py (CORRIGIDO)
from bottle import Bottle
from .user_controller import user_routes
from .home_controller import HomeController
from .studify_controller import studify_routes

def init_controllers(app: Bottle):
    # Inicializar HomeController passando o app principal
    HomeController(app) 
    
    # Merge das rotas dos usuários e studify.
    # O prefixo é desnecessário porque as rotas já têm o prefixo (e.g., /users/login, /studify)
    app.merge(user_routes)      # <-- CORRETO: SEM prefix=
    app.merge(studify_routes)   # <-- CORRETO: SEM prefix=