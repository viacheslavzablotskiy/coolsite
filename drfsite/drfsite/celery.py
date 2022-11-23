from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# установить модуль насторек Django по умолчанию для программы "Celery"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drfsite.settings')
app = Celery('drfsite')
# Использование строки здесь означает, что паботнику не нужно будет мариновать обьект при использовании Windows
app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()


# @app.task(bind=True)
# def debug_task(self):
#     print('Request:{0!r}'.format(self.request))
