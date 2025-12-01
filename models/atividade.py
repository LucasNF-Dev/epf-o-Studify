import os
import json

class Atividade:
    def __init__(self, id, user_id, nome, descricao, data, concluida):
        self.id = id
        self.user_id = user_id
        self.nome = nome
        self.descricao = descricao
        self.data = data
        self.concluida = concluida


    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'nome': self.nome,
            'descricao': self.descricao,
            'data': self.data,
            'concluida': self.concluida
        }
    

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
    

class AtividadeModel:
    def __init__(self):
        self.data = {}


    def get_file(self, user_id):
        print("CRIANDO PASTA SE NÃO EXISTIR")
        os.makedirs("data", exist_ok=True)
        file = f"data/atividades_{user_id}.json"
        print("FILE PATH:", file)
        return file
    

    def get_all(self, user_id):
        file = self.get_file(user_id)
        if not os.path.exists(file):
            return []
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return [Atividade.from_dict(item) for item in data]
        
    
    def save_all(self, user_id, atividades):
        file = self.get_file(user_id)
        os.makedirs("data", exist_ok=True)

        with open(file, "w", encoding="utf-8") as f:
            json.dump([a.to_dict() for a in atividades], f, indent=4, ensure_ascii=False)


    def get_by_id(self, user_id, atividade_id):
        atividades = self.get_all(user_id)
        return next((a for a in atividades if a.id == atividade_id), None)
    

    def next_id(self, user_id):
        atividades = self.get_all(user_id)
        if not atividades:
            return 1
        return max(a.id for a in atividades) + 1
    

    def add(self, atividade):
        atividades = self.get_all(atividade.user_id)
        atividades.append(atividade)
        self.save_all(atividade.user_id, atividades)
    

    def update(self, atividade):
        atividades = self.get_all(atividade.user_id)
        for i, a in enumerate(atividades):
            if a.id == atividade.id:
                atividades[i] = atividade
                break
        self.save_all(atividade.user_id, atividades)
    

    def delete(self, user_id, atividade_id):
        atividades = self.get_all(user_id)
        atividades = [a for a in atividades if a.id != atividade_id]
        self.save_all(user_id, atividades)
    
