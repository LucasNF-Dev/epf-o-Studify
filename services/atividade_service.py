from bottle import request
from models.atividade import AtividadeModel, Atividade

class AtividadeService:
    def __init__(self):
        self.atividade_model = AtividadeModel()

    def get_all(self):
        return self.atividade_model.get_all()

    def save(self):
        last_id = max([a.id for a in self.atividade_model.get_all()], default=0)
        new_id = last_id + 1
        nome = request.forms.get('nome')
        descricao = request.forms.get('descricao')
        data = request.forms.get('data')
        feita = request.forms.get('feita') == 'on'
        atividade = Atividade(new_id, nome, descricao, data, feita)
        self.atividade_model.add(atividade)

    def get_by_id(self, atividade_id):
        return self.atividade_model.get_by_id(atividade_id)

    def edit(self, atividade):
        atividade.nome = request.forms.get('nome')
        atividade.descricao = request.forms.get('descricao')
        atividade.data = request.forms.get('data')
        atividade.feita = request.forms.get('feita') == 'on'
        self.atividade_model.update(atividade)

    def delete(self, atividade_id):
        self.atividade_model.delete(atividade_id)