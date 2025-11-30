from bottle import Bottle, request
from controllers.base_controller import BaseController
from services.flashcard_service import FlashcardService
import random


class FlashcardController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.flashcard_service = FlashcardService()
        self.setup_routes()

    def setup_routes(self):

        self.app.route('/', method='GET', callback=self.listar)
        self.app.route('/novo', method='GET', callback=self.novo_form)
        self.app.route('/novo', method='POST', callback=self.novo_salvar)
        self.app.route('/revisar', method='GET', callback=self.revisar)
        self.app.route('/revisar/<card_id:int>/<nivel:int>',
                       method='GET',
                       callback=self.revisar_resposta)
        self.app.route('/<id:int>/editar', method='GET', callback=self.editar_form)
        self.app.route('/<id:int>/editar', method='POST', callback=self.editar_salvar)
        self.app.route('/<id:int>/excluir', method='GET', callback=self.excluir)
        self.app.route('/estudar', method='GET', callback=self.estudo_menu)
        self.app.route('/estudar', method='POST', callback=self.estudo_iniciar)
        self.app.route('/estudar/proximo', method='GET', callback=self.estudo_proximo)


    def listar(self):
        cards = self.flashcard_service.listar()
        return self.render('flashcard/listar', flashcards=cards)

    def novo_form(self):
        categorias = self.flashcard_service.listar_categorias()
        return self.render("flashcard/novo", categorias=categorias)

    def novo_salvar(self):
        pergunta = request.forms.get("pergunta")
        resposta = request.forms.get("resposta")
        categoria = request.forms.get("categoria")

        if categoria == "outro":
            categoria = request.forms.get("categoria_nova")

        if not pergunta or not resposta or not categoria:
            categorias = self.flashcard_service.listar_categorias()
            return self.render(
                "flashcard/novo",
                categorias=categorias,
                error="Todos os campos são obrigatórios."
            )

        self.flashcard_service.criar(pergunta, resposta, categoria)
        return self.redirect("/flashcards")

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
        return self.redirect("/flashcards/revisar")

    def editar_form(self, id):
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

    def estudo_menu(self):
        categorias = self.flashcard_service.listar_categorias()
        total = len(self.flashcard_service.listar())
        return self.render("flashcard/estudo_menu", categorias=categorias, total=total)

    def estudo_iniciar(self):
        categoria = request.forms.get("categoria")
        quantidade = request.forms.get("quantidade")
        ordem = request.forms.get("ordem")

        quantidade = int(quantidade) if quantidade.isdigit() else 9999

        cards = self.flashcard_service.listar()

        if categoria != "todas":
            cards = [c for c in cards if c.categoria == categoria]

        cards = cards[:quantidade]

        if ordem == "aleatoria":
            random.shuffle(cards)

        self.set_session("estudo_lista", [c.id for c in cards])
        self.set_session("estudo_pos", 0)

        return self.redirect("/flashcards/estudar/proximo")

    def estudo_proximo(self):
        lista = self.get_session("estudo_lista")
        pos = self.get_session("estudo_pos")

        if not lista or pos is None:
            return self.redirect("/flashcards/estudar")

        if pos >= len(lista):
            return self.render("flashcard/estudo_fim")

        card_id = lista[pos]
        card = self.flashcard_service.pegar_por_id(card_id)

        self.set_session("estudo_pos", pos + 1)

        return self.render("flashcard/estudo_card",
                           card=card, atual=pos+1, total=len(lista))

flashcard_routes = Bottle()
flashcard_controller = FlashcardController(flashcard_routes)
