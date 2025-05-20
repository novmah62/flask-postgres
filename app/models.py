from database import db

class Task(db.Model):
    __tablename__ = "tasks"
    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    status      = db.Column(db.String(30), nullable=False, default="pending")

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
