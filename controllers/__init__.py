# controllers/__init__.py

from bottle import Bottle
from .user_controller import create_user_routes 
from .home_controller import HomeController
from .studify_controller import studify_routes
from .flashcard_controller import flashcard_routes 
from .schedule_controller import schedule_routes # 🟢 NOVO IMPORT

user_routes = create_user_routes() 

def init_controllers(app: Bottle):
    HomeController(app)
    
    app.merge(user_routes)  
    app.merge(studify_routes)
    app.merge(flashcard_routes)
    app.merge(schedule_routes) # 🟢 NOVO MERGE: Rotas de Cronograma