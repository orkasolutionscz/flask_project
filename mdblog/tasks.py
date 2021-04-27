from mdblog import celery
from mdblog.models import Newsletter
from time import sleep

@celery.task
def notify_newsletter():
    subscribers = Newsletter.query.all()
    for subscriber in subscribers:
        print("Sending email to {}".format(subscriber.email))
        sleep(3)
