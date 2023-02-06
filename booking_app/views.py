from django.shortcuts import render
from django.views import generic
from .models import Appointment


class ViewAppointments(generic.ListView):
    model = Appointment
    queryset = Appointment.objects.order_by('-date')
    template_name = 'appointments.html'
    paginate_by = 9
