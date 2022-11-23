
from __future__ import absolute_import, unicode_literals
from celery import shared_task, Celery

from celery.schedules import crontab
from django.core.mail import EmailMessage
celery = Celery('tasks', broker='pyamqp://guest@localhost//')
import os
os.environ['DJANGO_SETTING_MODULE'] = 'drfsite.setting'
@shared_task
def adding_task(x, y):
    return x + y
# def send_shipment_email(owner_name, order_name, owner_email):
#     mail_subject = "Your order is ready"
#     message = "Hello {0}, your order {1} is ready to be shipped\n Kindly have patience.\n regards.".format(
#         owner_name, order_name
#     )
#     email = EmailMessage(mail_subject, message, to=[owner_email])
#     email.send()
