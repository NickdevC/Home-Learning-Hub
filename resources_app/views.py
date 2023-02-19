from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Resource
# from .forms import AppointmentForm
from django.contrib import messages
from django.urls import reverse

class DisplayResource(generic.ListView):
    model = Resource
    queryset = Resource.objects.all().order_by('-created_on')
    template_name = 'resources.html'
    context_object_name = 'resource_items'
    paginate_by = 9
