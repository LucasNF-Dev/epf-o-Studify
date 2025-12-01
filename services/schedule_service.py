from models.schedule_event import ScheduleModel, ScheduleEvent
from datetime import datetime
import time

# Formato padrão usado para armazenar datas no Model
DATE_FORMAT = "%Y-%m-%dT%H:%M" 

class ScheduleService:
    def __init__(self):
        self.model = ScheduleModel()

    def get_all_by_user(self, user_id: int):
        """Retorna todos os eventos do usuário."""
        return self.model.get_all_by_user_id(user_id)

    def add_new_event(self, user_id: int, title: str, start_time: str, end_time: str, description: str = None):
        """Adiciona um novo evento, validando se o horário de início é anterior ao fim."""
        
        start_dt = datetime.strptime(start_time, DATE_FORMAT)
        end_dt = datetime.strptime(end_time, DATE_FORMAT)
        
        if start_dt >= end_dt:
            raise ValueError("O horário de início deve ser anterior ao horário de término.")
            
        last_id = max([e.id for e in self.model.events], default=0)
        new_id = last_id + 1
        
        event = ScheduleEvent(
            id=new_id, 
            user_id=user_id, 
            title=title, 
            start_time=start_time, 
            end_time=end_time, 
            description=description
        )
        self.model.add_event(event)
        return event

    def get_next_activity(self, user_id: int):
        """
        Encontra a próxima atividade agendada a partir do momento atual.
        """
        now = datetime.now()
        
        # 1. Obter todos os eventos
        all_events = self.get_all_by_user(user_id)
        
        # 2. Converter start_time para objetos datetime e filtrar eventos passados
        upcoming_events = []
        for event in all_events:
            try:
                event_start_dt = datetime.strptime(event.start_time, DATE_FORMAT)
                # Inclui apenas eventos que começam no futuro ou estão acontecendo agora
                if event_start_dt >= now:
                    upcoming_events.append((event_start_dt, event))
            except ValueError:
                # Ignora eventos com formato de data inválido
                continue
        
        if not upcoming_events:
            return None # Nenhuma atividade futura
            
        # 3. Encontrar o evento mais próximo (o que tem o menor datetime de início)
        upcoming_events.sort(key=lambda x: x[0])
        
        # Retorna o objeto evento (índice 1 da tupla)
        return upcoming_events[0][1]