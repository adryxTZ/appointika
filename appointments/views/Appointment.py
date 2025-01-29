from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from appointments.models.appointment import Appointment
from appointments.serializers.appointment import AppointmentSerializer


class AppointmentView(APIView):

    def get(self, request, pk=None):
        if pk:
            try:
                appointment = Appointment.objects.get(pk=pk)
                serializer = AppointmentSerializer(appointment)
                return Response(serializer.data)
            except Appointment.DoesNotExist:
                return Response({"error": "Appointment not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            if request.user.role == 'doctor':
                appointments = Appointment.objects.filter(doctor__user=request.user)
            elif request.user.role == 'patient':
                appointments = Appointment.objects.filter(patient__user=request.user)
            else:
                appointments = Appointment.objects.all()

            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        try:
            appointment = Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AppointmentSerializer(appointment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            appointment = Appointment.objects.get(pk=pk)
            appointment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Appointment.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
