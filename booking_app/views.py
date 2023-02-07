from django.shortcuts import render
from django.views import generic
from .models import Appointment


# Render index.html
def index(request):
    """ Return homepage """
    return render(request, 'index.html')


# Render appointments.html
class AppointmentList(generic.ListView):
    """
    Render appointment list from the database
    """
    model = Appointment
    template_name = 'appointments.html'
    context_object_name = 'appointment_items'

    def get_queryset(self):

        queryset = {
            'appointment_details': Appointment.objects.all()
        }
        return queryset


# Render appointment cards in appointments.html
class ViewAppointments(generic.ListView):
    model = Appointment
    queryset = Appointment.objects.order_by('-date')
    template_name = 'appointments.html'
    paginate_by = 9
