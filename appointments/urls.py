from django.urls import path

from appointments.views.Appointment import AppointmentView

urlpatterns = [
    path('', AppointmentView.as_view(), name='appointments-list'),
    path('<int:pk>/', AppointmentView.as_view(), name='appointment-detail'),
]
