from flask import Flask
from database import init_db, db
from app.routes import bp as task_bp

def create_app():
    app = Flask(__name__)
    init_db(app)
    with app.app_context():
        db.create_all()      # auto-create tables in dev
    app.register_blueprint(task_bp)
    return app
