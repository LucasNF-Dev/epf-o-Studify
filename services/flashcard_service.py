from models.flashcard import Flashcard
from .data_manager import load_data, save_data, get_next_id 
from datetime import datetime, timedelta

class FlashcardService:

    @staticmethod
    def _map_to_object(data):
        if not data: return None
        return Flashcard(
            id=data.get('id'),
            pergunta=data.get('pergunta'),
            resposta=data.get('resposta'),
            nivel=data.get('nivel', 1),
            ultima_revisao=data.get('ultima_revisao', datetime.now().strftime("%Y-%m-%d")),
            proxima_revisao=data.get('proxima_revisao', datetime.now().strftime("%Y-%m-%d")),
            categoria=data.get('categoria', "Geral")
        )


    @staticmethod
    def criar(pergunta, resposta, categoria):
        flashcards = load_data()
        novo_id = get_next_id(flashcards)
        proxima = datetime.now().strftime("%Y-%m-%d")

        novo_card_dict = {
            'id': novo_id,
            'pergunta': pergunta,
            'resposta': resposta,
            'categoria': categoria,
            'nivel': 1,
            'ultima_revisao': proxima,
            'proxima_revisao': proxima
        }
        
        flashcards.append(novo_card_dict)
        save_data(flashcards)

    @staticmethod
    def listar():
        flashcards_data = load_data()
        return [FlashcardService._map_to_object(d) for d in flashcards_data]
    
    @staticmethod
    def pegar_por_id(id):
        flashcards = load_data()
        for data in flashcards:
            if data['id'] == id:
                return FlashcardService._map_to_object(data)
        return None

    @staticmethod
    def atualizar(id, pergunta, resposta, categoria):
        flashcards = load_data()
        for i, data in enumerate(flashcards):
            if data['id'] == id:
                flashcards[i]['pergunta'] = pergunta
                flashcards[i]['resposta'] = resposta
                flashcards[i]['categoria'] = categoria
                save_data(flashcards)
                return True
        return False

    @staticmethod
    def excluir(id):
        flashcards = load_data()
        flashcards_atualizada = [data for data in flashcards if data['id'] != id]
        
        if len(flashcards_atualizada) < len(flashcards):
            save_data(flashcards_atualizada)
            return True
        return False

    @staticmethod 
    def pegar_para_revisao():
        flashcards_data = load_data()
        hoje = datetime.now().strftime("%Y-%m-%d")

        cards_para_revisar = []
        for data in flashcards_data:
            if data.get('proxima_revisao', '2999-01-01') <= hoje:
                 cards_para_revisar.append(FlashcardService._map_to_object(data))
        
        cards_para_revisar.sort(key=lambda x: x.proxima_revisao)
        return cards_para_revisar
    
    @staticmethod 
    def revisar(id, dificuldade):
        flashcards = load_data()
        
        dias = {1: 3, 2: 2, 3: 1}[dificuldade]
        proxima = (datetime.now() + timedelta(days=dias)).strftime("%Y-%m-%d")
        ultima = datetime.now().strftime("%Y-%m-%d")

        for i, data in enumerate(flashcards):
            if data['id'] == id:
                flashcards[i]['nivel'] = dificuldade
                flashcards[i]['ultima_revisao'] = ultima
                flashcards[i]['proxima_revisao'] = proxima
                save_data(flashcards)
                return True
        return False

    @staticmethod
    def listar_categorias():
        flashcards = load_data()
        categorias_existentes = {data.get('categoria', 'Geral') for data in flashcards if data.get('categoria')}
        categorias_padrao = ["Matemática", "Programação", "Inglês", "Biologia", "Gramática", "História"]
        todas = list(dict.fromkeys(categorias_padrao + list(categorias_existentes)))
        return todas