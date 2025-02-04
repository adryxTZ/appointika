from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

from user.views.userRegistration import UserRegistrationView

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path("userRegistration", UserRegistrationView.as_view(), name="userRegistration"),
]
