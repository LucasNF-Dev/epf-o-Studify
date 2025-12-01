from bottle import Bottle
from .user_controller import create_user_routes      # 🟢 Importa a função
from .home_controller import HomeController
from .studify_controller import studify_routes       # A variável studify_routes ainda é definida no final do seu studify_controller.py

# 🟢 EXECUÇÃO E MESCLAGEM: Chamamos a função aqui para obter as rotas de usuário.
user_routes = create_user_routes() 

def init_controllers(app: Bottle):
    # Inicializar HomeController (configura rotas diretamente no app principal)
    HomeController(app)
    
    # Merge das rotas do usuário e do dashboard (sub-aplicações Bottle)
    # Não usamos 'prefix' pois os caminhos já são completos (e.g., /users/login)
    
    # 1. Rotas do Usuário (login, register, profile, edit)
    app.merge(user_routes)  
    
    # 2. Rotas do Dashboard (studify, logout)
    app.merge(studify_routes)