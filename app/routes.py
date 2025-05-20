from flask import Blueprint, request, jsonify
from app.service import TaskService

bp = Blueprint("tasks", __name__, url_prefix="/tasks")
svc = TaskService()

@bp.route("", methods=["POST"])
def create_task():
    t = svc.create(request.get_json() or {})
    return jsonify(t.to_dict()), 201

@bp.route("", methods=["GET"])
def list_tasks():
    return jsonify([t.to_dict() for t in svc.list()]), 200

@bp.route("/<int:task_id>", methods=["GET"])
def get_task(task_id):
    t = svc.get(task_id)
    return jsonify(t.to_dict()), 200

@bp.route("/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    t = svc.update(task_id, request.get_json() or {})
    return jsonify(t.to_dict()), 200

@bp.route("/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    svc.delete(task_id)
    return jsonify({"message": "Deleted"}), 200
