from flask import Blueprint, request, jsonify
from app.controllers.job_controller import JobController

job_bp = Blueprint('job_bp', _name_)

job_controller = JobController()

@job_bp.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = job_controller.get_all_jobs()
    return jsonify(jobs)

@job_bp.route('/job', methods=['POST'])
def create_job():
    data = request.get_json()
    job = job_controller.create_job(
        data['title'], data['description'], data['company'],
        data['location'], data['salary']
    )
    return jsonify(job), 201

@job_bp.route('/job/<int:job_id>', methods=['GET'])
def get_job(job_id):
    job = job_controller.get_job(job_id)
    return jsonify(job)

@job_bp.route('/job/<int:job_id>', methods=['PUT'])
def update_job(job_id):
    data = request.get_json()
    job = job_controller.update_job(
        job_id, data['title'], data['description'], data['company'],
        data['location'], data['salary']
    )
    return jsonify(job)

@job_bp.route('/job/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    response, status_code = job_controller.delete_job(job_id)
    return jsonify(response), status_code
