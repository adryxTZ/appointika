from django.db import models
from rest_framework import serializers

from doctors.models import DoctorProfile
from user.models import User


class DoctorRegistrationSerializer(serializers.ModelSerializer):
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()
    available_days = models.JSONField()

    class Meta:
        model = User
        # child_model = DoctorProfile
        fields = ['email', 'password', 'first_name', 'last_name']
        # child_fields = ['specialization', 'experience', 'available_days']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['username'] = validated_data['email']  # Set username as email
        user = User.objects.create_user(**validated_data)
        user.role = 'doctor'  # Set role as doctor
        user.save()
        return user

