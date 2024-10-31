from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from appointments.models import Appointment
from appointments.decorators import active_subscription_required

@active_subscription_required
def dashboard_view(request):
    available_appointments = Appointment.objects.filter(is_booked=False, date__gt=timezone.now()).order_by('date', 'court')

    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        appointment = Appointment.objects.get(pk=appointment_id)
        appointment.user_id = request.user
        appointment.is_booked = True
        appointment.save()

    return render(request, "dashboard/main.html", {'appointments_list': available_appointments})