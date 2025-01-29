from rest_framework import serializers

from appointments.models.appointment import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
        depth = 1
