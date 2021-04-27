import os

DEBUG = True
SQLALCHEMY_DATABASE_URI = "sqlite:////home/spravce/Python/flask_project/blog.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# EMAIL ACCOUNT
EMAIL_USERNAME = os.environ.get("MDBLOG_EMAIL_USERNAME", None)
EMAIL_PASSWORD = os.environ.get("MDBLOG_EMAIL_PASSWORD", None)
