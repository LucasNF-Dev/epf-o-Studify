from bottle import Bottle, request, redirect, template
from config import Config
from .base_controller import BaseController
from services.schedule_service import ScheduleService, DATE_FORMAT
from datetime import datetime, timedelta

class ScheduleController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.schedule_service = ScheduleService()
        self.setup_routes()

    def get_logged_in_user_id(self):
        user_id_str = request.get_cookie("user_id", secret=Config.SECRET_KEY)
        try:
            return int(user_id_str)
        except:
            return None

    def secure_route(self, callback):
        """Decorador para proteger rotas."""
        def wrapper(*args, **kwargs):
            user_id = self.get_logged_in_user_id()
            if not user_id:
                return self.redirect('/users/login')
            return callback(user_id, *args, **kwargs)
        return wrapper

    def setup_routes(self):
        self.app.route('/schedule', method='GET', callback=self.secure_route(self.schedule_view))
        self.app.route('/schedule/add', method=['GET', 'POST'], callback=self.secure_route(self.add_event))

    def schedule_view(self, user_id):
        """Exibe o calendário/lista de eventos."""
        all_events = self.schedule_service.get_all_by_user(user_id)
        
        # Converter string de data para objeto datetime para facilitar a ordenação/exibição
        parsed_events = []
        for event in all_events:
            try:
                start_dt = datetime.strptime(event.start_time, DATE_FORMAT)
                end_dt = datetime.strptime(event.end_time, DATE_FORMAT)
                parsed_events.append((start_dt, end_dt, event))
            except ValueError:
                continue # Ignora eventos inválidos

        # Ordenar por data de início
        parsed_events.sort(key=lambda x: x[0])
        
        # Formatar para exibição no TPL
        events_for_view = [
            {
                'title': e[2].title,
                'description': e[2].description,
                'start': e[0].strftime('%d/%m %H:%M'),
                'end': e[1].strftime('%H:%M')
            } for e in parsed_events
        ]
        
        return self.render('schedule_view', events=events_for_view)

    def add_event(self, user_id):
        """Adiciona um novo evento ao cronograma."""
        
        # Define um valor padrão para 'agora' no formato esperado do input datetime-local
        now_str = datetime.now().strftime('%Y-%m-%dT%H:%M') 
        later_str = (datetime.now() + timedelta(hours=1)).strftime('%Y-%m-%dT%H:%M')
        
        if request.method == 'GET':
            return self.render('schedule_add_form', 
                                 title='', 
                                 description='', 
                                 start_time=now_str, 
                                 end_time=later_str, 
                                 error=None)
        
        # POST
        title = request.forms.get('title')
        description = request.forms.get('description')
        start_time = request.forms.get('start_time') # Vem como YYYY-MM-DDTHH:MM
        end_time = request.forms.get('end_time')

        try:
            self.schedule_service.add_new_event(user_id, title, start_time, end_time, description)
            return self.redirect('/schedule') 
            
        except ValueError as e:
            # Erro de validação (ex: horário de início > horário de fim)
            return self.render('schedule_add_form', 
                                 title=title, 
                                 description=description, 
                                 start_time=start_time, 
                                 end_time=end_time, 
                                 error=str(e))
        except Exception as e:
            return self.render('schedule_add_form', 
                                 title=title, 
                                 description=description, 
                                 start_time=start_time, 
                                 end_time=end_time, 
                                 error="Erro ao salvar evento. Tente novamente.")


# Ponto de entrada do controller para o __init__.py
schedule_routes = Bottle()
ScheduleController(schedule_routes)