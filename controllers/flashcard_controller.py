from bottle import request, Bottle
from .base_controller import BaseController
from services.flashcard_service import FlashcardService
from datetime import datetime


class FlashcardController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.flashcard_service = FlashcardService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/', method='GET', callback=self.listar)
        self.app.route('/novo', method=['GET', 'POST'], callback=self.novo)
        self.app.route('/revisar', method=['GET', 'POST'], callback=self.revisar)
        self.app.route('/revisar/<card_id:int>/<nivel:int>', method='GET', callback=self.revisar_resposta)
        self.app.route('/<id:int>/editar', method='GET', callback=self.editar)
        self.app.route('/<id:int>/editar', method='POST', callback=self.editar_salvar)
        self.app.route('/<id:int>/excluir', method='GET', callback=self.excluir)

    def listar(self):
        cards = self.flashcard_service.listar()
        return self.render('flashcard/listar', flashcards=cards)

    def novo(self):
        if request.method == 'GET':
            categorias = self.flashcard_service.listar_categorias()
            return self.render('flashcard/novo', categorias=categorias)

        pergunta = request.forms.get("pergunta")
        resposta = request.forms.get("resposta")
        categoria = request.forms.get("categoria")

        if categoria == "outro":
            categoria = request.forms.get("categoria_nova")

        if not pergunta or not resposta or not categoria:
            categorias = self.flashcard_service.listar_categorias()
            return self.render(
                'flashcard/novo',
                categorias=categorias,
                error="Todos os campos são obrigatórios."
            )

        self.flashcard_service.criar(pergunta, resposta, categoria)

        return self.redirect('/flashcards')

    def revisar(self):
        cards = self.flashcard_service.pegar_para_revisao()

        if not cards:
            todos = self.flashcard_service.listar()
            return self.render(
                "flashcard/listar",
                flashcards=todos,
                mensagem="Não há mais flashcards para revisar hoje!"
            )

        return self.render("flashcard/revisar", card=cards[0])

    def revisar_resposta(self, card_id, nivel):
        self.flashcard_service.revisar(card_id, nivel)
        return self.redirect('/flashcards/revisar')

    def editar(self, id):
        flashcard = self.flashcard_service.pegar_por_id(id)
        categorias = self.flashcard_service.listar_categorias()

        return self.render("flashcard/editar", flashcard=flashcard, categorias=categorias)

    def editar_salvar(self, id):
        pergunta = request.forms.get("pergunta")
        resposta = request.forms.get("resposta")
        categoria = request.forms.get("categoria")

        self.flashcard_service.atualizar(id, pergunta, resposta, categoria)

        return self.redirect("/flashcards")

    def excluir(self, id):
        self.flashcard_service.excluir(id)
        return self.redirect("/flashcards")


flashcard_routes = Bottle()
flashcard_controller = FlashcardController(flashcard_routes)
