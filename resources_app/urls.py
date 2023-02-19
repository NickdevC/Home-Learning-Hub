from .import views
from django.urls import path


urlpatterns = [
    path('resources_app/', views.DisplayResource.as_view(), name='resources'),
]
