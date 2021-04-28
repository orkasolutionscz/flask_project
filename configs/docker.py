SQLALCHEMY_DATABASE_URI = "postgres://docker:docker@database"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# EMAIL ACCOUNT
EMAIL_USERNAME = "salon.pesvice@gmail.com"
EMAIL_PASSWORD = "eQKMAt96sl2@"

SECRET_KEY = b'\xfcc\x01n\xed\xa9\x88\x9a\x08\xf3\x1a}R\xeb=/\\\xc1\xbc\xe4\x11,\xa2\xa2'

# CELERY CONFIG
BROKER_URL = "pyamqp://quest@rabbitmq//"
