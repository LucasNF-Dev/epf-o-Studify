from bottle import route, run, request, redirect, template, response, Bottle
from config import Config
from .base_controller import BaseController 
from services.user_service import UserService

class UserController(BaseController):
    def __init__(self, app): 
        # app é a instância 'user_routes' neste caso
        super().__init__(app)
        self.user_service = UserService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/users/login', method=['GET', 'POST'], callback=self.login)
        self.app.route('/users/register', method=['GET', 'POST'], callback=self.register)
        self.app.route('/users/profile', method='GET', callback=self.profile)
        self.app.route('/users/edit/<user_id:int>', method=['GET', 'POST'], callback=self.edit_user)
        # self.app.route('/users/delete/<user_id:int>', method='POST', callback=self.delete_user)

    def login(self):
        if request.method == 'GET':
            return self.render('login', error=None, email=None)
            
        # 1. OBTER DADOS DO FORMULÁRIO
        email = request.forms.get('email')
        password = request.forms.get('password')
        
        # 2. VALIDAÇÃO BÁSICA
        if not email or not password:
            return self.render('login', error="Email e senha são obrigatórios", email=email)
            
        # 3. AUTENTICAÇÃO (Usa hashing no Service)
        user = self.user_service.login(email, password)
        
        if user:
            # 4. Configurar Cookies
            response.set_cookie("user_id", str(user.id), 
                                 secret=Config.SECRET_KEY, 
                                 httponly=True, 
                                 path='/')
            response.set_cookie("user_name", user.name, 
                                 secret=Config.SECRET_KEY, 
                                 httponly=True, 
                                 path='/')
            
            # 5. Redirecionamento 
            return self.redirect("/studify")
        else:
            return self.render('login', error="Email ou senha inválidos.", email=email)
            
    def register(self):
        if request.method == 'GET':
            return self.render('register', 
                                 error=None, 
                                 name='', 
                                 email='', 
                                 birthdate='')
        else: # POST
            name = request.forms.get('name')
            email = request.forms.get('email')
            birthdate = request.forms.get('birthdate')
            password = request.forms.get('password')

            try:
                self.user_service.register(name, email, birthdate, password)
                return self.redirect('/users/login') 
            except ValueError as e:
                return self.render('register', 
                                     error=str(e), 
                                     name=name, 
                                     email=email, 
                                     birthdate=birthdate)
            except Exception as e:
                print(f"ERRO INESPERADO NO REGISTRO: {str(e)}")
                return self.render('register', 
                                     error=f"Erro interno: {type(e).__name__} - {str(e)}", 
                                     name=name, 
                                     email=email, 
                                     birthdate=birthdate)

    def profile(self):
        user_id_str = request.get_cookie("user_id", secret=Config.SECRET_KEY)
        
        if not user_id_str:
            return self.redirect('/users/login')
        
        try:
            user = self.user_service.get_by_id(int(user_id_str))
        except Exception:
             user = None

        if not user:
            response.delete_cookie("user_id", secret=Config.SECRET_KEY)
            return self.redirect('/users/login')

        user_data = {
            'name': user.name,
            'email': user.email,
            'birthdate': user.birthdate,
            'id': user.id
        }
        
        return self.render('profile', user=user_data) 

    def edit_user(self, user_id: int):
        user = self.user_service.get_by_id(user_id)
        logged_user_id = request.get_cookie("user_id", secret=Config.SECRET_KEY)
        
        # 1. VERIFICAÇÃO DE SEGURANÇA
        if not user or str(user_id) != logged_user_id:
            return self.redirect('/studify')

        # --- REQUISIÇÃO GET: Mostrar formulário ---
        if request.method == 'GET':
            return self.render('user_edit_form', 
                                 user_id=user.id,
                                 name=user.name,
                                 email=user.email,
                                 birthdate=user.birthdate,
                                 error=None)

        # --- REQUISIÇÃO POST: Salvar alterações ---
        if request.method == 'POST':
            name = request.forms.get('name')
            email = request.forms.get('email')
            birthdate = request.forms.get('birthdate')
            new_password = request.forms.get('new_password')
            
            try:
                # Chama o Service para atualizar
                self.user_service.edit_user(user, name, email, birthdate, new_password)
                return self.redirect('/users/profile')
                
            except ValueError as e:
                return self.render('user_edit_form', 
                                     user_id=user.id,
                                     name=name,
                                     email=email,
                                     birthdate=birthdate,
                                     error=str(e))
                                     
            except Exception as e:
                print(f"ERRO CRÍTICO ao editar usuário {user.id}: {str(e)}")
                return self.render('user_edit_form', 
                                     user_id=user.id,
                                     name=name,
                                     email=email,
                                     birthdate=birthdate,
                                     error=f"Erro interno: Não foi possível salvar as alterações. ({type(e).__name__})")

# Ponto de entrada corrigido: Usa função para criar a instância Bottle
def create_user_routes() -> Bottle:
    user_routes_app = Bottle()
    UserController(user_routes_app) 
    return user_routes_app