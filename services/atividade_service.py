from bottle import request
from config import Config
from models.atividade import AtividadeModel, Atividade

class AtividadeService:
    def __init__(self):
        self.atividade_model = AtividadeModel()

    def get_user_id(self):
        user_id = request.get_cookie('user_id', secret=Config.SECRET_KEY)
        if not user_id:
            raise Exception("Nenhum usuário logado")
        return int(user_id)
    

    def get_all(self):
        user_id = self.get_user_id()
        return self.atividade_model.get_all(user_id)


    def save(self):
        user_id = request.get_cookie('user_id', secret=Config.SECRET_KEY)

        if not user_id:
            raise Exception("Sem usuario logado")
        
        user_id = int(user_id)

        atividades_user = self.atividade_model.get_all(user_id)
        last_id = max([a.id for a in atividades_user], default=0)
        new_id = last_id + 1

        nome = request.forms.get('nome')
        descricao = request.forms.get('descricao')
        data = request.forms.get('data')
        concluida = request.forms.get('concluida') == 'on'

        atividade = Atividade(new_id, user_id, nome, descricao, data, concluida)

        self.atividade_model.add(atividade, user_id)


    def get_by_id(self, atividade_id):
        return self.atividade_model.get_by_id(atividade_id)


    def edit(self, atividade):
        atividade.nome = request.forms.get('nome')
        atividade.descricao = request.forms.get('descricao')
        atividade.data = request.forms.get('data')
        atividade.concluida = request.forms.get('concluida') == 'on'
        self.atividade_model.update(atividade)


    def delete(self, atividade_id):
        self.atividade_model.delete(atividade_id)