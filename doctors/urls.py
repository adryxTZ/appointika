from django.urls import path

from doctors.views.doctor import DoctorView

urlpatterns = [
    path('', DoctorView.as_view(), name='doctors-list'),
    path('<int:pk>/', DoctorView.as_view(), name='doctor-detail'),
]
