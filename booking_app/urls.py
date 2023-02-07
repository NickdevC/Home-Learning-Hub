from .import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('appointments/', views.ViewAppointments.as_view(), name='appointments'),
]