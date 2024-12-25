from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the app
app = Flask(__name__)

# Set the app config for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///job_vacancies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Import routes after initializing the app and db
from app.routes.job_routes import job_bp
app.register_blueprint(job_bp)
