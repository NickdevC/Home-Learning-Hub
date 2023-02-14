from django.shortcuts import render, redirect
from django.views import generic
from .models import Appointment
from .forms import AppointmentForm
from django.contrib import messages


# Render index.html and appointment form
def index(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            human = True
            messages.success(request, f"Thanks for making an appointment, we\
                will email you soon to confirm.")
            return redirect('index')
        else:
            messages.error(request, f"CAPTCHA Invalid. Letters are case\
                sensitive. Please try again.")
    return render(request, 'index.html', {'form': form})


# Render appointment cards in appointments.html
class ViewAppointments(generic.ListView):
    model = Appointment
    queryset = Appointment.objects.all().order_by('-date')
    template_name = 'appointments.html'
    context_object_name = 'appointment_items'
    paginate_by = 9
