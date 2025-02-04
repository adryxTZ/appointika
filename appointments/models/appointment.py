from django.db import models

from choices.account_choices import STATUS_TYPE_CHOICES
from doctors.models import DoctorProfile

from user.models import User


class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'patient'})
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, blank=False, null=False)
    appointment_time = models.DateTimeField()

    APPOINTMENT_STATUS = [
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed")]

    appointment_status = models.CharField(max_length=10, choices=APPOINTMENT_STATUS, default="Pending")
    status = models.CharField(max_length=200, blank=False, null=False, choices=STATUS_TYPE_CHOICES, default="ACTIVE")
    created_at = models.DateTimeField(auto_now=True)
