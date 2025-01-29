from django.db import models

from appointika import settings
from choices.account_choices import STATUS_TYPE_CHOICES
from user.models import User


class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'role': 'doctor'})
    specialization = models.CharField(max_length=100, blank=False, null=False)
    experience = models.IntegerField()
    available_days = models.JSONField()
    status = models.CharField(max_length=200, blank=False, null=False, choices=STATUS_TYPE_CHOICES, default="ACTIVE")
    created_at = models.DateTimeField(auto_now=True)
