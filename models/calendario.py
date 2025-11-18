from models.prova import Prova
from models.evento import Evento

class Calendario:
    def __init__(self, comeco, fim):
        self.__comeco = comeco
        self.__fim = fim
        self.__datas_provas = []
        self.__datas_importantes = []
        
    def add_prova(self, data, materia):
        self.__datas_provas.append(Prova(data, materia))

    def add_evento(self, data, titulo, descricao=""):
        self.__datas_importantes.append(Evento(data, titulo, descricao))

    def get_provas_por_data(self, data):
        provas = [p for p in self.__datas_provas if p.data == data]
        return provas if provas else []

    def get_eventos_por_data(self, data):
        eventos = [e for e in self.__datas_importantes if e.data == data]
        return eventos if eventos else []