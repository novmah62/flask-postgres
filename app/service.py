from flask import abort
from app.models import Task
from app.repository import TaskRepository

class TaskService:
    def __init__(self):
        self.repo = TaskRepository()

    def create(self, data: dict) -> Task:
        if "title" not in data:
            abort(400, "Missing field 'title'")
        task = Task(**data)
        return self.repo.add(task)

    def list(self):
        return self.repo.list_all()

    def get(self, task_id: int) -> Task:
        task = self.repo.get_by_id(task_id)
        if not task:
            abort(404, "Task not found")
        return task

    def update(self, task_id: int, data: dict) -> Task:
        task = self.get(task_id)
        for k, v in data.items():
            if hasattr(task, k):
                setattr(task, k, v)
        self.repo.commit()
        return task

    def delete(self, task_id: int):
        task = self.get(task_id)
        self.repo.delete(task)
