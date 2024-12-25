from app import db
from app.models.job_post import JobPost

class JobService:

    def create_job(self, title, description, company, location, salary):
        new_job = JobPost(title=title, description=description, company=company, location=location, salary=salary)
        db.session.add(new_job)
        db.session.commit()
        return new_job.to_dict()
    
    def get_all_jobs(self):
        jobs = JobPost.query.all()
        return [job.to_dict() for job in jobs]
    
    def get_job(self, job_id):
        job = JobPost.query.get(job_id)
        if job:
            return job.to_dict()
        return {"error": "Job not found"}, 404
    
    def update_job(self, job_id, title, description, company, location, salary):
        job = JobPost.query.get(job_id)
        if job:
            job.title = title
            job.description = description
            job.company = company
            job.location = location
            job.salary = salary
            db.session.commit()
            return job.to_dict()
        return {"error": "Job not found"}, 404
    
    def delete_job(self, job_id):
        job = JobPost.query.get(job_id)
        if job:
            db.session.delete(job)
            db.session.commit()
            return {"message": "Job deleted successfully"}, 200
        return {"error": "Job not found"}, 404
