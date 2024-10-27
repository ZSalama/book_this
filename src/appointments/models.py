from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import time
import pytz

class Appointment(models.Model):
	TIME_CHOICES = [
		(time(13, 0), '1:00 PM'),
		(time(14, 0), '2:00 PM'),
		(time(15, 0), '3:00 PM'),
		(time(16, 0), '4:00 PM'),
	]

	COURT_CHOICES = [
		(1, 'Court 1'),
		(2, 'Court 2'),
		(3, 'Court 3'),
		(4, 'Court 4'),
	]

	appointment_id = models.AutoField(primary_key=True)
	date = models.DateField(default=timezone.now)
	time = models.TimeField(choices=TIME_CHOICES, default=TIME_CHOICES[0][0])
	court = models.IntegerField(choices=COURT_CHOICES)
	notes = models.TextField(blank=True, null=True)
	user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	is_booked = models.BooleanField(default=False)

	def __str__(self):
		return f"Appointment {self.appointment_id} on {self.date} at {self.time} (Court {self.court})"