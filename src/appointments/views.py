from django.shortcuts import render
from appointments.models import Appointment
#from django.contrib.auth.decorators import login_required
from .decorators import active_subscription_required
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

#@active_subscription_required
@login_required
def my_appointments_view(request):
    #appointments = Appointment.objects.filter(user_id=request.user)
    appointments = Appointment.objects.filter(user_id=request.user, date__gt=timezone.now()).order_by('date', 'court')
    return render(request, 'appointments/my_appointments.html', {'appointments_list': appointments})