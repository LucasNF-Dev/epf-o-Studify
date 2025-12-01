import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

# 🟢 Definição dos status do Kanban
STATUS_TODO = 'todo'
STATUS_IN_PROGRESS = 'in_progress'
STATUS_DONE = 'done'

class Task:
    def __init__(self, id, user_id, title, status=STATUS_TODO, description=""):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.description = description
        self.status = status

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'description': self.description,
            'status': self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            user_id=data['user_id'],
            title=data['title'],
            description=data.get('description', ''),
            status=data.get('status', STATUS_TODO)
        )

class TaskModel:
    FILE_PATH = os.path.join(DATA_DIR, 'tasks.json')

    def __init__(self):
        self.tasks = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Task.from_dict(item) for item in data]

    def _save(self):
        os.makedirs(DATA_DIR, exist_ok=True) 
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=4, ensure_ascii=False)

    def get_all_by_user_id(self, user_id: int):
        return [t for t in self.tasks if t.user_id == user_id]

    def get_by_id(self, task_id: int):
        return next((t for t in self.tasks if t.id == task_id), None)

    def add_task(self, task: Task):
        self.tasks.append(task)
        self._save()

    def update_task(self, updated_task: Task):
        for i, task in enumerate(self.tasks):
            if task.id == updated_task.id and task.user_id == updated_task.user_id:
                self.tasks[i] = updated_task
                self._save()
                return True
        return False