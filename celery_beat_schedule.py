# alx_travel_app_0x03/celery_beat_schedule.py
from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'check-pending-bookings': {
        'task': 'listings.tasks.check_pending_bookings',
        'schedule': crontab(minute='*/30'),  # Every 30 minutes
    },
    'send-booking-reminders': {
        'task': 'listings.tasks.send_booking_reminders',
        'schedule': crontab(hour=9, minute=0),  # Daily at 9 AM
    },
}
