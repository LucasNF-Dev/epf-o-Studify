import os
import json

class Atividade:
    def __init__(self, id, nome, descricao, data, feita):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.data = data
        self.feita = feita

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'data': self.data,
            'feita': self.feita
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(**data)
    
class AtividadeModel:
    FILE_PATH = 'data/atividades.json'

    def __init__(self):
        self.atividades = self._load()

    def _load(self):
        import json, os
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            return [Atividade.from_dict(item) for item in json.load(f)]

    def _save(self):
        import json
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([a.to_dict() for a in self.atividades], f, indent=5, ensure_ascii=False)

    def get_all(self):
        return self.atividades

    def get_by_id(self, atividade_id):
        return next((a for a in self.atividades if a.id == atividade_id), None)

    def add(self, atividade):
        self.atividades.append(atividade)
        self._save()

    def update(self, updated_atividade):
        for i, a in enumerate(self.atividades):
            if a.id == updated_atividade.id:
                self.atividades[i] = updated_atividade
                self._save()
                break

    def delete(self, atividade_id):
        self.atividades = [a for a in self.atividades if a.id != atividade_id]
        self._save()
    
