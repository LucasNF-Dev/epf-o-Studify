from bottle import Bottle, request
from .base_controller import BaseController
from services.atividade_service import AtividadeService

class AtividadeController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.atividade_service = AtividadeService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/atividades', method='GET', callback=self.list_atividades)
        self.app.route('/atividades/add', method=['GET', 'POST'], callback=self.add_atividade)
        self.app.route('/atividades/edit/<atividade_id:int>', method=['GET', 'POST'], callback=self.edit_atividade)
        self.app.route('/atividades/delete/<atividade_id:int>', method='POST', callback=self.delete_atividade)

    def list_atividades(self):
        atividades = self.atividade_service.get_all()
        return self.render('atividades', atividades=atividades)

    def add_atividade(self):
        if request.method == 'GET':
            return self.render('atividade_form', atividade=None, action='/atividades/add')
        else:
            self.atividade_service.save()
            self.redirect('/atividades')

    def edit_atividade(self, atividade_id):
        atividade = self.atividade_service.get_by_id(atividade_id)
        if request.method == 'GET':
            return self.render('atividade_form', atividade=atividade, action=f'/atividades/edit/{atividade_id}')
        else:
            self.atividade_service.edit(atividade)
            self.redirect('/atividades')

    def delete_atividade(self, atividade_id):
        self.atividade_service.delete(atividade_id)
        self.redirect('/atividades')

atividade_routes = Bottle()
atividade_controller = AtividadeController(atividade_routes)