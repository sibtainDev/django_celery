import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')
app = Celery('quick_publisher')
app.config_from_object('django.conf:settings')
app.conf.broker_url = 'redis://localhost:6379'
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))