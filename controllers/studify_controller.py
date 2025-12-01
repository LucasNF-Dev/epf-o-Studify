from bottle import route, request, redirect, response, Bottle, template
# Importe o BaseController e a Configuração
from config import Config
from .base_controller import BaseController 
from services.user_service import UserService # Necessário para buscar o User pelo ID

class StudifyController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.user_service = UserService() # Para buscar o usuário pelo ID do cookie
        # Inicialize outros services que você precisará (FlashcardService, CalendarService)
        # self.flashcard_service = FlashcardService() 
        self.setup_routes()

    def setup_routes(self):
        # Rota que o login está redirecionando
        self.app.route('/studify', method='GET', callback=self.studify_dashboard)
        self.app.route('/logout', method='GET', callback=self.logout) # Rota de Logout

    def get_logged_in_user(self):
        """Função auxiliar para verificar o cookie e retornar o objeto User."""
        from config import Config # Importe Config aqui para garantir escopo

        # Tenta obter o ID do cookie seguro
        user_id_str = request.get_cookie("user_id", secret=Config.SECRET_KEY)
        
        # LINHA DE DEBUG:
        print(f"DEBUG - Cookie 'user_id' lido: {user_id_str}") 
        
        if not user_id_str:
            return None

        # Busca o objeto User no banco de dados/Service
        try:
            # O MÉTODO 'get_by_id' DEVE EXISTIR NO UserService
            user = self.user_service.get_by_id(int(user_id_str)) 
            return user
        except Exception as e:
            # Em caso de erro (ex: ID inválido), trata como não logado
            print(f"Erro ao buscar usuário pelo cookie: {e}")
            return None

    def studify_dashboard(self):
        user = self.get_logged_in_user()
        
        if not user:
            # Se não estiver logado, redireciona para o login
            return redirect('/users/login') 
            
        # 3. Lógica para Coletar Dados (Busca nos Services)
        # Ex: total_cards = self.flashcard_service.get_total_for_user(user.id)
        
        # Dados de exemplo para o template:
        data_for_view = {
            'user_name': user.name,
            'total_flashcards': 42, # Mock
            'upcoming_events': 3,    # Mock
            'next_event': 'Revisão Matemática', # Mock
        }
        
        # 4. Renderiza o template studify.tpl
        return self.render('studify', **data_for_view) 
    
    def logout(self):
        # Apaga o cookie do navegador
        response.delete_cookie("user_id", secret=Config.SECRET_KEY)
        response.delete_cookie("user_name", secret=Config.SECRET_KEY)
        # Redireciona para a página de login
        return redirect('/users/login')

# Ponto de entrada do controller para o __init__.py
studify_routes = Bottle()
studify_controller = StudifyController(studify_routes)