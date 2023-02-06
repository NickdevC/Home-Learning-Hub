from django.shortcuts import render
from django.views import generic
from .models import Appointment


# Render index.html
def index(request):
    """ Return homepage """
    return render(request, 'index.html')


class ViewAppointments(generic.ListView):
    model = Appointment
    queryset = Appointment.objects.order_by('-date')
    template_name = 'appointments.html'
    paginate_by = 9
