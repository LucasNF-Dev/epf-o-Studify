from bottle import Bottle, request, redirect, template
from config import Config
from .base_controller import BaseController
from services.task_service import TaskService
from models.task import STATUS_TODO, STATUS_IN_PROGRESS, STATUS_DONE # Para referenciar os status

class TaskController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.task_service = TaskService()
        self.setup_routes()

    def get_logged_in_user_id(self):
        """Função auxiliar para obter o ID do usuário logado."""
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
        # 1. Visualização do Quadro Kanban
        self.app.route('/tasks', method='GET', callback=self.secure_route(self.kanban_board))
        
        # 2. Criação de Tarefas
        self.app.route('/tasks/add', method=['GET', 'POST'], callback=self.secure_route(self.add_task))
        
        # 3. Ação para Mover Tarefa entre colunas (POST)
        self.app.route('/tasks/move/<task_id:int>', method='POST', callback=self.secure_route(self.move_task))

    def kanban_board(self, user_id):
        """Exibe o quadro Kanban."""
        board = self.task_service.get_all_by_user(user_id)
        
        # Define os nomes das colunas para o template
        column_names = {
            STATUS_TODO: "A Fazer",
            STATUS_IN_PROGRESS: "Em Andamento",
            STATUS_DONE: "Concluído"
        }
        
        return self.render('kanban_board', 
                             board=board,
                             column_names=column_names,
                             # Passa as chaves dos status para o template
                             STATUS_TODO=STATUS_TODO, 
                             STATUS_IN_PROGRESS=STATUS_IN_PROGRESS,
                             STATUS_DONE=STATUS_DONE)

    def add_task(self, user_id):
        """Adiciona uma nova tarefa."""
        if request.method == 'GET':
            return self.render('task_add_form', title='', description='', error=None)
        
        # POST
        title = request.forms.get('title')
        description = request.forms.get('description', '')
        
        try:
            self.task_service.add_new_task(user_id, title, description)
            return self.redirect('/tasks')
        except ValueError as e:
            return self.render('task_add_form', title=title, description=description, error=str(e))
    
    def move_task(self, user_id, task_id):
        """Move uma tarefa para um novo status (coluna)."""
        new_status = request.forms.get('new_status')
        
        try:
            self.task_service.change_status(user_id, task_id, new_status)
        except ValueError as e:
            # Em caso de erro (tarefa não encontrada/status inválido), apenas loga ou ignora.
            print(f"Erro ao mover tarefa {task_id}: {e}")
        
        return self.redirect('/tasks')


# Ponto de entrada do controller para o __init__.py
task_routes = Bottle()
TaskController(task_routes)