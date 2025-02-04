from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from doctors.models import DoctorProfile
from doctors.serializers.doctor import DoctorProfileSerializer
from user.serializers.doctorRegistration import DoctorRegistrationSerializer


# ---- Doctor View ----
class DoctorView(APIView):
    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminUser()]
        return [AllowAny()]  # Adjust permission for other methods if needed

    def get(self, request, pk=None):
        if pk:
            try:
                doctor = DoctorProfile.objects.get(pk=pk)
                serializer = DoctorProfileSerializer(doctor)
                return Response(serializer.data)
            except DoctorProfile.DoesNotExist:
                return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Search Doctors
            specialization = request.query_params.get('specialization', None)
            name = request.query_params.get('name', None)
            doctors = DoctorProfile.objects.all()

            if specialization:
                doctors = doctors.filter(specialization__icontains=specialization)
            if name:
                doctors = doctors.filter(Q(user__first_name__icontains=name) | Q(user__last_name__icontains=name))

            serializer = DoctorProfileSerializer(doctors, many=True)
            return Response(serializer.data)

    # def post(self, request):
    #     serializer = DoctorProfileSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = DoctorRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            specialization = request.data['specialization']
            experience = request.data['experience']
            available_days = request.data['available_days']

            # Create DoctorProfile
            DoctorProfile.objects.create(
                user=user,
                specialization=specialization,
                experience=experience,
                available_days=available_days
            )

            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        try:
            doctor = DoctorProfile.objects.get(pk=pk)
        except DoctorProfile.DoesNotExist:
            return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = DoctorProfileSerializer(doctor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            doctor = DoctorProfile.objects.get(pk=pk)
            doctor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except DoctorProfile.DoesNotExist:
            return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)
