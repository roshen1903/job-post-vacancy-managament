from flask import Blueprint, jsonify

# Define the Blueprint correctly using _name_
job_bp = Blueprint('job_bp', __name__)

@job_bp.route('/jobs', methods=['GET'])
def get_jobs():
    return jsonify({"message": "List of jobs"})
