import os
import django
from django.utils import timezone
from datetime import timedelta, time

from pytz import timezone as pytz_timezone

# Define the Eastern Time Zone
eastern_tz = pytz_timezone('America/New_York')

def populate_appointments():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_backend.settings')
    django.setup()

    from appointments.models import Appointment

    # Get the current date in the Eastern time zone
    current_date = timezone.now().astimezone(eastern_tz).date()

    TIME_CHOICES = [
        (time(13, 0), '1:00 PM'),
        (time(14, 0), '2:00 PM'),
        (time(15, 0), '3:00 PM'),
        (time(16, 0), '4:00 PM'),
    ]

    COURT_CHOICES = [1, 2, 3, 4]

    for day in range(7):  # Next 7 days
        appointment_date = current_date + timedelta(days=day)
        for court in COURT_CHOICES:
            for time_choice in TIME_CHOICES:
                # Create the appointment
                Appointment.objects.create(
                    date=appointment_date,
                    time=time_choice[0],
                    court=court,
                    is_booked=False,
                    notes=f"Available appointment on {appointment_date} at {time_choice[1]} for Court {court}"
                )

    print("Appointments populated successfully!")

if __name__ == "__main__":
    populate_appointments()