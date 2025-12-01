# controllers/user_controller.py

from bottle import route, run, request, redirect, template, response, Bottle
from config import Config
from .base_controller import BaseController 
from services.user_service import UserService

class UserController(BaseController):
    def __init__(self, app): 
        super().__init__(app)
        self.user_service = UserService()
        self.setup_routes()

    def setup_routes(self):
        # self.app.route('/users', method='GET', callback=self.list_users)
        self.app.route('/users/login', method=['GET', 'POST'], callback=self.login)
        self.app.route('/users/register', method=['GET', 'POST'], callback=self.register)
        # Rotas de CRUD (add, edit, delete)
        # self.app.route('/users/add', method=['GET', 'POST'], callback=self.add_user)
        # self.app.route('/users/edit/<user_id:int>', method=['GET', 'POST'], callback=self.edit_user)
        # self.app.route('/users/delete/<user_id:int>', method='POST', callback=self.delete_user)

    def list_users(self):
        users = self.user_service.get_all()
        return self.render('users', users=users)

    def login(self):
        if request.method == 'GET':
            return self.render('login', error=None, email=None)
            
        # 1. OBTER DADOS DO FORMULÁRIO (CORRETO)
        email = request.forms.get('email')
        password = request.forms.get('password') # <-- LINHA FALTANTE ADICIONADA!
        
        # 2. VALIDAÇÃO BÁSICA
        if not email or not password:
            return self.render('login', error="Email e senha são obrigatórios", email=email)
            
        # 3. AUTENTICAÇÃO
        user = self.user_service.login(email, password)
        
        if user:
            # 1. Configurar Cookies (ADICIONE 'path=/')
            # Garantimos que o cookie é válido para todo o domínio (/)
            response.set_cookie("user_id", str(user.id), 
                                 secret=Config.SECRET_KEY, 
                                 httponly=True, 
                                 path='/') # <-- ADICIONE ISSO
            
            response.set_cookie("user_name", user.name, 
                                 secret=Config.SECRET_KEY, 
                                 httponly=True, 
                                 path='/') # <-- ADICIONE ISSO
            
            # 2. Redirecionamento 
            return self.redirect("/studify")
        else:
            # 5. FALHA NA AUTENTICAÇÃO
            return self.render('login', error="Email ou senha inválidos.", email=email)
            
    def register(self):
        if request.method == 'GET':
            # GET: retorna o formulário vazio
            return self.render('register', 
                                error=None, 
                                name='', 
                                email='', 
                                birthdate='')
        else: # POST
            # 1. Obter todos os dados do formulário ANTES de qualquer TRY/EXCEPT
            # Isso garante que todas essas variáveis estejam no escopo da função
            name = request.forms.get('name')
            email = request.forms.get('email')
            birthdate = request.forms.get('birthdate')
            password = request.forms.get('password')

            try:
                # 2. Tentar registrar
                # Se houver um erro, ele será capturado abaixo, mas as variáveis
                # de formulário (name, email, birthdate) estarão no escopo para renderizar
                self.user_service.register(name, email, birthdate, password)
                
                # Sucesso
                return self.redirect('/users/login') 
                
            except ValueError as e:
                # Trata erros de validação (ex: email já existe)
                return self.render('register', 
                                     error=str(e), 
                                     name=name, 
                                     email=email, 
                                     birthdate=birthdate)
            except Exception as e:
                # Trata erros inesperados e renderiza com os dados preenchidos
                print(f"ERRO INESPERADO NO REGISTRO: {str(e)}")
                return self.render('register', 
                                     error=f"Erro interno: {type(e).__name__} - {str(e)}", 
                                     name=name, 
                                     email=email, 
                                     birthdate=birthdate)
# Ponto de entrada do controller para o __init__.py
# ESTAS DUAS LINHAS RESOLVEM O 'ImportError'
user_routes = Bottle()
user_controller = UserController(user_routes)