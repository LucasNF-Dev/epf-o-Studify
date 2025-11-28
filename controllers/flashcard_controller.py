from bottle import request, Bottle
from .base_controller import BaseController
from services.flashcard_service import FlashcardService

class FlashcardController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.flashcard_service = FlashcardService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/', method='GET', callback=self.listar)
        self.app.route('/novo', method=['GET', 'POST'], callback=self.novo)
        self.app.route('/revisar', method=['GET', 'POST'], callback=self.revisar)
        self.app.route('/revisar/<card_id:int>/<nivel:int>',
                       method='GET', callback=self.revisar_resposta)

    def listar(self):
        cards = self.flashcard_service.listar()
        return self.render('flashcard/listar', flashcards=cards)

    def novo(self):
        if request.method == 'GET':
            return self.render('flashcard/novo')

        pergunta = request.forms.get("pergunta")
        resposta = request.forms.get("resposta")

        if not pergunta or not resposta:
            return self.render('flashcard/novo',
                               error="Todos os campos são obrigatórios")

        self.flashcard_service.criar(pergunta, resposta)
        return self.redirect('/flashcards')

    def revisar(self):
        cards = self.flashcard_service.pegar_para_revisao()

        if not cards:
            todos = self.flashcard_service.listar()
            return self.render("flashcard/listar", flashcards=todos, mensagem="Não há mais flashcards para revisar hoje!")
        return self.render("flashcard/revisar", card=cards[0])

    def revisar_resposta(self, card_id, nivel):
        self.flashcard_service.revisar(card_id, nivel)
        return self.redirect('/flashcards/revisar')


flashcard_routes = Bottle()
flashcard_controller = FlashcardController(flashcard_routes)
