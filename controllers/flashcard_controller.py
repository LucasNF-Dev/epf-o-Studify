from bottle import Bottle, request, redirect, template
from config import Config
from .base_controller import BaseController
from services.flashcard_service import FlashcardService
from services.user_service import UserService # Para obter o usuário logado

class FlashcardController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.flashcard_service = FlashcardService()
        self.user_service = UserService()
        self.setup_routes()

    def get_logged_in_user_id(self):
        """Função auxiliar para obter o ID do usuário logado (usado em /studify)."""
        user_id_str = request.get_cookie("user_id", secret=Config.SECRET_KEY)
        try:
            return int(user_id_str)
        except:
            return None

    def secure_route(self, callback):
        """Decorador básico para proteger rotas contra usuários não logados."""
        def wrapper(*args, **kwargs):
            user_id = self.get_logged_in_user_id()
            if not user_id:
                return self.redirect('/users/login')
            return callback(user_id, *args, **kwargs)
        return wrapper

    def setup_routes(self):
        # Rotas para gerenciamento e criação de cartões
        self.app.route('/flashcards', method='GET', callback=self.secure_route(self.list_cards))
        self.app.route('/flashcards/add', method=['GET', 'POST'], callback=self.secure_route(self.add_card))
        
        # Rotas para a sessão de revisão
        self.app.route('/flashcards/review', method='GET', callback=self.secure_route(self.start_review))
        self.app.route('/flashcards/check/<card_id:int>', method='POST', callback=self.secure_route(self.process_review))

    # --- Visão Geral (CRUD) ---

    def list_cards(self, user_id):
        """Exibe todos os flashcards do usuário."""
        cards = self.flashcard_service.get_all_by_user(user_id)
        return self.render('flashcards_list', cards=cards)

    def add_card(self, user_id):
        """Adiciona um novo cartão."""
        if request.method == 'GET':
            return self.render('flashcard_add_form', front='', back='', error=None)
        
        # POST
        front = request.forms.get('front')
        back = request.forms.get('back')
        
        if not front or not back:
            return self.render('flashcard_add_form', front=front, back=back, 
                                 error="Frente e verso do cartão são obrigatórios.")

        self.flashcard_service.add_new_card(user_id, front, back)
        return self.redirect('/flashcards')

    # --- Sessão de Revisão (Anki-like) ---
    
    def start_review(self, user_id):
        """Inicia a sessão de revisão, mostrando o próximo cartão."""
        cards_due = self.flashcard_service.get_cards_due_today(user_id)
        
        if not cards_due:
            # Se não há cartões para revisar
            return self.render('flashcards_review_finished')

        # Pega o primeiro cartão da fila para revisão
        current_card = cards_due[0]
        
        # Renderiza a frente do cartão
        return self.render('flashcards_review_card', 
                             card=current_card, 
                             show_back=False)

    def process_review(self, user_id, card_id):
        """Processa a resposta do usuário e atualiza o agendamento."""
        
        card = self.flashcard_service.get_card_by_id(card_id)
        quality = int(request.forms.get('quality')) # 0-5
        
        if not card or card.user_id != user_id:
            # Cartão não encontrado ou não pertence ao usuário
            return self.redirect('/flashcards') 

        # 1. Se quality == -1 (Botão "Mostrar Resposta")
        if quality == -1:
             # Renderiza o verso do cartão, mantendo os botões de avaliação
             return self.render('flashcards_review_card', 
                                  card=card, 
                                  show_back=True)
        
        # 2. Se quality >= 0 (Botões de Avaliação 0-5)
        # Calcula o novo agendamento com base na avaliação do usuário
        self.flashcard_service.calculate_next_schedule(card, quality)
        
        # Redireciona para a próxima revisão (recarrega /flashcards/review)
        return self.redirect('/flashcards/review')


# Ponto de entrada do controller para o __init__.py
flashcard_routes = Bottle()
flashcard_controller = FlashcardController(flashcard_routes)