from rest_framework import serializers

from doctors.models import DoctorProfile


class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = "__all__"
        depth = 1
