from django.shortcuts import render
from appointments.models import Appointment
#from django.contrib.auth.decorators import login_required
from .decorators import active_subscription_required

# Create your views here.

@active_subscription_required
def my_appointments_view(request):
    appointments = Appointment.objects.filter(user_id=request.user)
    return render(request, 'appointments/my_appointments.html', {'appointments_list': appointments})
