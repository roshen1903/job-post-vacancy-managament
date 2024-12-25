from app.services.job_service import JobService

class JobController:

    def create_job(self, title, description, company, location, salary):
        job_service = JobService()
        return job_service.create_job(title, description, company, location, salary)
    
    def get_all_jobs(self):
        job_service = JobService()
        return job_service.get_all_jobs()
    
    def get_job(self, job_id):
        job_service = JobService()
        return job_service.get_job(job_id)
    
    def update_job(self, job_id, title, description, company, location, salary):
        job_service = JobService()
        return job_service.update_job(job_id, title, description, company, location, salary)
    
    def delete_job(self, job_id):
        job_service = JobService()
        return job_service.delete_job(job_id)
