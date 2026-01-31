import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'iitm-placement-portal-secret-key-2025'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///placement_portal.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'static/uploads/resumes'
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024
    ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}