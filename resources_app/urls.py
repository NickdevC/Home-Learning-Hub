from .import views
from django.urls import path


urlpatterns = [
    path('resources/', views.DisplayResource.as_view(), name='resources'),
]
