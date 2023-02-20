from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Resource
from .forms import ResourceForm
from django.contrib import messages
from django.urls import reverse


# Render all resources for unauthenticated user
class DisplayResource(generic.ListView):
    model = Resource
    queryset = Resource.objects.all().order_by('-created_on')
    template_name = 'resources.html'
    context_object_name = 'resource_items'
    paginate_by = 9


# Allow authenticated user to upload resources and display them
def uploadResource(request):
    form = ResourceForm()
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            human = True
            messages.success(request, f"Resource uploaded successfully!")
            return redirect('edit_resources')
        else:
            messages.error(request, f"Error: Could not upload file.")
    return render(request, 'edit_resources.html', {'form': form})
