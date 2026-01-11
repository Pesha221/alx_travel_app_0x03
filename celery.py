# alx_travel_app_0x03/celery.py
import os
from celery import Celery

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app_0x03.settings')

# Create Celery app instance
app = Celery('alx_travel_app_0x03')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# Configuration from Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
    
