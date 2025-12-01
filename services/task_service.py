from models.task import TaskModel, Task, STATUS_TODO, STATUS_IN_PROGRESS, STATUS_DONE

class TaskService:
    def __init__(self):
        self.model = TaskModel()

    def get_all_by_user(self, user_id: int):
        """Retorna todas as tarefas do usuário, agrupadas por status."""
        all_tasks = self.model.get_all_by_user_id(user_id)
        
        # Agrupa as tarefas em um dicionário para o quadro Kanban
        kanban_board = {
            STATUS_TODO: [t for t in all_tasks if t.status == STATUS_TODO],
            STATUS_IN_PROGRESS: [t for t in all_tasks if t.status == STATUS_IN_PROGRESS],
            STATUS_DONE: [t for t in all_tasks if t.status == STATUS_DONE],
        }
        return kanban_board

    def add_new_task(self, user_id: int, title: str, description: str = ""):
        """Adiciona uma nova tarefa com status inicial 'todo'."""
        if not title:
            raise ValueError("O título da tarefa é obrigatório.")
            
        last_id = max([t.id for t in self.model.tasks], default=0)
        new_id = last_id + 1
        
        task = Task(new_id, user_id, title, description=description)
        self.model.add_task(task)
        return task

    def change_status(self, user_id: int, task_id: int, new_status: str):
        """Muda o status (coluna) de uma tarefa específica."""
        task = self.model.get_by_id(task_id)

        if not task or task.user_id != user_id:
            raise ValueError("Tarefa não encontrada ou acesso negado.")
            
        if new_status not in [STATUS_TODO, STATUS_IN_PROGRESS, STATUS_DONE]:
            raise ValueError("Status inválido.")
            
        task.status = new_status
        self.model.update_task(task)
        return task

    def get_task_by_id(self, task_id: int):
        return self.model.get_by_id(task_id)