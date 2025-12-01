import json
import os
from datetime import datetime

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class ScheduleEvent:
    """Representa um evento ou compromisso no calendário do usuário."""
    def __init__(self, id, user_id, title, 
                 start_time: str, end_time: str, 
                 description=None):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.description = description
        
        # As datas são armazenadas como strings (ISO format) para fácil serialização
        self.start_time = start_time 
        self.end_time = end_time

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'description': self.description,
            'start_time': self.start_time,
            'end_time': self.end_time
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            user_id=data['user_id'],
            title=data['title'],
            description=data.get('description'),
            start_time=data['start_time'],
            end_time=data['end_time']
        )

class ScheduleModel:
    FILE_PATH = os.path.join(DATA_DIR, 'schedule_events.json')

    def __init__(self):
        self.events = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [ScheduleEvent.from_dict(item) for item in data]

    def _save(self):
        os.makedirs(DATA_DIR, exist_ok=True) 
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([e.to_dict() for e in self.events], f, indent=4, ensure_ascii=False)

    def get_all_by_user_id(self, user_id: int):
        return [e for e in self.events if e.user_id == user_id]

    def add_event(self, event: ScheduleEvent):
        self.events.append(event)
        self._save()

    def update_event(self, updated_event: ScheduleEvent):
        for i, event in enumerate(self.events):
            # Garante que estamos atualizando o mesmo evento do mesmo usuário
            if event.id == updated_event.id and event.user_id == updated_event.user_id:
                self.events[i] = updated_event
                self._save()
                break
    def delete_event(self, event_id: int, user_id: int):
        # Filtra a lista, removendo o evento com o ID e user_id correspondente
        self.events = [e for e in self.events if not (e.id == event_id and e.user_id == user_id)]
        self._save()