class Evento:
    def __init__(self, data, titulo, descricao=""):
        self.data = data
        self.titulo = titulo
        self.descricao = descricao

    def to_dict(self):
        return{
            "data": self.data,
            "titulo": self.titulo,
            "descricao": self.descricao
        }
    
    @staticmethod
    def from_dict(d):
        return Evento(d["data"], d["titulo"], d.get("descricao", ""))