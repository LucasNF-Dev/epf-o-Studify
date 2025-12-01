from bottle import route, request, redirect, response, Bottle, template
from config import Config
from .base_controller import BaseController 
from services.user_service import UserService 

# 🟢 NOVOS IMPORTS DE SERVICES
# Necessários para contar itens no dashboard
from services.flashcard_service import FlashcardService 
from services.schedule_service import ScheduleService 
from services.task_service import TaskService 
from models.task import STATUS_DONE, STATUS_IN_PROGRESS, STATUS_TODO # Para contar tarefas ativas

class StudifyController(BaseController):
    def __init__(self, app):
        # 🟢 CORREÇÃO CRUCIAL: Chama o construtor da classe base
        super().__init__(app) 
        
        self.user_service = UserService()
        
        # 🟢 INICIALIZAÇÃO DOS SERVICES (Resolve o AttributeError)
        self.flashcard_service = FlashcardService()
        self.schedule_service = ScheduleService()
        self.task_service = TaskService()
        
        self.setup_routes()

    def setup_routes(self):
        # Rota que o login está redirecionando
        self.app.route('/studify', method='GET', callback=self.studify_dashboard)
        self.app.route('/logout', method='GET', callback=self.logout) # Rota de Logout

    def get_logged_in_user(self):
        """Função auxiliar para verificar o cookie e retornar o objeto User."""
        # Importamos Config aqui APENAS se não estivesse no topo (mas está, então podemos remover esta linha se estiver duplicada)
        # from config import Config 

        user_id_str = request.get_cookie("user_id", secret=Config.SECRET_KEY)
        
        # LINHA DE DEBUG (mantida)
        print(f"DEBUG - Cookie 'user_id' lido: {user_id_str}") 
        
        if not user_id_str:
            return None

        # Busca o objeto User no banco de dados/Service
        try:
            user = self.user_service.get_by_id(int(user_id_str)) 
            return user
        except Exception as e:
            print(f"Erro ao buscar usuário pelo cookie: {e}")
            return None

    def studify_dashboard(self):
        user = self.get_logged_in_user()
        
        if not user:
            return redirect('/users/login')
        
        # 1. Obter dados básicos e ID
        user_name = request.get_cookie("user_name", secret=Config.SECRET_KEY)
        user_id = user.id 
        
        # 🟢 2. Coleta de Dados Reais dos Módulos
        
        # Flashcards
        all_flashcards = self.flashcard_service.get_all_by_user(user_id)
        
        # Cronograma
        next_event = self.schedule_service.get_next_activity(user_id)
        all_schedule_events = self.schedule_service.get_all_by_user(user_id)
        
        # Kanban
        kanban_board = self.task_service.get_all_by_user(user_id)
        
        # Conta tarefas ativas (TODO + IN_PROGRESS)
        total_tasks_active = len(kanban_board[STATUS_TODO]) + len(kanban_board[STATUS_IN_PROGRESS])
        
        # 🟢 3. Dados para a View
        data_for_view = {
            'user_name': user_name or user.name,
            
            # Flashcards
            'total_flashcards': len(all_flashcards),
            
            # Cronograma
            'upcoming_events': len(all_schedule_events), 
            'next_event_title': next_event.title if next_event else 'Nenhuma agendada',
            
            # Kanban
            'total_tasks': total_tasks_active,
        }
        
        return self.render('studify', data_for_view=data_for_view)
    
    def logout(self):
        # Apaga o cookie do navegador
        response.delete_cookie("user_id", secret=Config.SECRET_KEY)
        response.delete_cookie("user_name", secret=Config.SECRET_KEY)
        # Redireciona para a página de login
        return redirect('/users/login')

# Ponto de entrada do controller para o __init__.py
studify_routes = Bottle()
studify_controller = StudifyController(studify_routes)