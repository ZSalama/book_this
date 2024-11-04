import os
import django
from django.utils import timezone
from datetime import timedelta, time



def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_backend.settings')
    django.setup()

    from appointments.models import Appointment
    # Get the current date and time, and calculate one week into the future
    future_date = timezone.now().date() + timedelta(days=7)

    # List of court and time choices from your model
    court_choices = [1, 2, 3, 4]
    time_choices = [
        time(13, 0),  # 1:00 PM
        time(14, 0),  # 2:00 PM
        time(15, 0),  # 3:00 PM
        time(16, 0)   # 4:00 PM
    ]

    # Loop through each combination of court and time, and create an appointment
    for court in court_choices:
        for appointment_time in time_choices:
            appointment = Appointment(
                date=future_date,
                time=appointment_time,
                court=court,
                notes='',  # Assuming no notes for now
                is_booked=False
            )
            appointment.save()

    #print("16 appointments have been added successfully.")

if __name__ == '__main__':
    main()