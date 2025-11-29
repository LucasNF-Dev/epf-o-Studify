from bottle import Bottle
from controllers.user_controller import user_routes
from controllers.atividade_controller import atividade_routes

def init_controllers(app: Bottle):
    app.merge(user_routes)
    app.merge(atividade_routes)
