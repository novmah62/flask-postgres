from app.models import Task
from database import db

class TaskRepository:
    def add(self, task: Task):
        db.session.add(task); db.session.commit(); return task

    def list_all(self):
        return Task.query.all()

    def get_by_id(self, task_id: int):
        return Task.query.get(task_id)

    def commit(self):
        db.session.commit()

    def delete(self, task: Task):
        db.session.delete(task); db.session.commit()
