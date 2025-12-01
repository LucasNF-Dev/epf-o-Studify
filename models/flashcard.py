import json
import os
import time # Para armazenar timestamps

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class Flashcard:
    def __init__(self, id, user_id, front, back, 
                 due_date=None, interval=0, ease=2.5):
        self.id = id
        self.user_id = user_id
        self.front = front
        self.back = back
        # Data limite para a próxima revisão (timestamp em segundos)
        self.due_date = due_date if due_date is not None else int(time.time())
        # Intervalo de tempo atual em dias
        self.interval = interval
        # Fator de facilidade (Easy Factor - EF), tipicamente começa em 2.5
        self.ease = ease

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'front': self.front,
            'back': self.back,
            'due_date': self.due_date,
            'interval': self.interval,
            'ease': self.ease
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            user_id=data['user_id'],
            front=data['front'],
            back=data['back'],
            due_date=data['due_date'],
            interval=data.get('interval', 0),
            ease=data.get('ease', 2.5)
        )

class FlashcardModel:
    FILE_PATH = os.path.join(DATA_DIR, 'flashcards.json')

    def __init__(self):
        self.flashcards = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Flashcard.from_dict(item) for item in data]

    def _save(self):
        # Garante que a pasta 'data' existe
        os.makedirs(DATA_DIR, exist_ok=True) 
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([c.to_dict() for c in self.flashcards], f, indent=4, ensure_ascii=False)

    def get_all(self):
        return self.flashcards

    def get_by_user_id(self, user_id: int):
        return [c for c in self.flashcards if c.user_id == user_id]

    def add_card(self, card: Flashcard):
        self.flashcards.append(card)
        self._save()

    def update_card(self, updated_card: Flashcard):
        for i, card in enumerate(self.flashcards):
            if card.id == updated_card.id and card.user_id == updated_card.user_id:
                self.flashcards[i] = updated_card
                self._save()
                break

    def delete_card(self, card_id: int, user_id: int):
        self.flashcards = [c for c in self.flashcards if c.id != card_id or c.user_id != user_id]
        self._save()