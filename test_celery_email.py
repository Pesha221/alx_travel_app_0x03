# test_celery_email.py
import os
import sys
import django

# Setup Django
sys.path.append('/home/abuaminuu/machine/alx_travel_app_0x03')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app_0x03.settings')
django.setup()

from listings.tasks import send_booking_confirmation_email

print("Testing Celery email task...")

# Create a test booking first (adjust ID based on your data)
test_booking_id = 1  # Change this to an actual booking ID

# Test the task
try:
    result = send_booking_confirmation_email.delay(test_booking_id)
    print(f"✓ Email task triggered successfully!")
    print(f"  Task ID: {result.id}")
    print(f"  Check Celery worker logs for progress")
    print(f"  Monitor at: http://localhost:5555")
except Exception as e:
    print(f"✗ Error: {e}")
    
