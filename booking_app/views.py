from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Appointment
from .forms import AppointmentForm
from django.contrib import messages
from django.urls import reverse


# Render index.html and appointment form
def index(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            human = True
            messages.success(request, f"Thanks for making an appointment, your\
                child's teacher will email you soon to confirm.")
            return redirect('index')
        else:
            messages.error(request, f"There was an error submitting your\
                appointment. Please try again.")
    return render(request, 'index.html', {'form': form})


# Render appointment cards in appointments.html
class ViewAppointments(generic.ListView):
    model = Appointment
    queryset = Appointment.objects.all().order_by('-date')
    template_name = 'appointments.html'
    context_object_name = 'appointment_items'
    paginate_by = 6


# Delete an appointment
def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    appointment.delete()
    messages.add_message(request, messages.SUCCESS, f"Appointment successfully\
        deleted!")
    return redirect('appointments')
