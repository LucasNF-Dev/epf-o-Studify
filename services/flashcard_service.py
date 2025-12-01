import time
from models.flashcard import FlashcardModel, Flashcard
import math
from datetime import datetime, timedelta

class FlashcardService:
    def __init__(self):
        self.model = FlashcardModel()

    def get_all_by_user(self, user_id: int):
        """Retorna todos os flashcards do usuário."""
        return self.model.get_by_user_id(user_id)

    def get_cards_due_today(self, user_id: int):
        """Retorna apenas os flashcards que devem ser revisados hoje."""
        now = int(time.time())
        all_cards = self.get_all_by_user(user_id)
        return [card for card in all_cards if card.due_date <= now]

    def add_new_card(self, user_id: int, front: str, back: str):
        """Adiciona um novo flashcard e define o agendamento inicial."""
        last_id = max([c.id for c in self.model.get_all()], default=0)
        new_id = last_id + 1
        
        # O novo cartão é agendado para HOJE (time.time()) com intervalo 0.
        card = Flashcard(new_id, user_id, front, back)
        self.model.add_card(card)
        return card

    # 🟢 ALGORITMO DE REPETIÇÃO ESPAÇADA (SuperMemo 2)
    def calculate_next_schedule(self, card: Flashcard, quality: int):
        """
        Calcula o próximo intervalo de repetição e o novo fator de facilidade (Ease Factor).
        quality (Qualidade da resposta): 
        - 0-1: Errou
        - 2: Difícil
        - 3: Bom
        - 4-5: Fácil/Muito Fácil
        """
        
        # 1. Ajuste do Fator de Facilidade (Ease Factor - EF)
        new_ease = card.ease + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
        
        # Garante que o fator de facilidade mínimo seja 1.3
        card.ease = max(1.3, new_ease)
        
        # 2. Cálculo do Novo Intervalo
        if quality >= 3:
            # Acertou: Aumenta o intervalo
            if card.interval == 0:
                # Primeira repetição correta: 1 dia
                new_interval = 1
            elif card.interval == 1:
                # Segunda repetição correta: 6 dias
                new_interval = 6
            else:
                # Repetições subsequentes: Intervalo anterior * Ease Factor
                new_interval = math.ceil(card.interval * card.ease)
        else:
            # Errou (quality < 3): Reinicia
            new_interval = 1
            # Redefine o Ease Factor para o padrão (pode ser opcional, mas ajuda na recuperação)
            # card.ease = max(1.3, card.ease - 0.2) 

        card.interval = new_interval
        
        # 3. Define a Próxima Data de Revisão
        if quality < 3:
             # Se errou, a revisão é agendada para hoje para correção imediata ou amanhã
             # Vamos agendar para amanhã (1 dia) para não sobrecarregar
             card.due_date = int(time.time() + (24 * 60 * 60)) # Agendar para amanhã
        else:
             # Agendamento normal baseado no novo intervalo (dias para segundos)
             seconds_to_add = card.interval * 24 * 60 * 60
             card.due_date = int(time.time() + seconds_to_add)

        # 4. Salva o cartão atualizado
        self.model.update_card(card)
        
    def get_card_by_id(self, card_id: int):
        """Busca um cartão específico pelo ID."""
        all_cards = self.model.get_all()
        return next((c for c in all_cards if c.id == card_id), None)