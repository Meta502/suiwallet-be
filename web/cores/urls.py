from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from cores.views.authentication import CustomerRegistrationView

AUTHENTICATION_URL_PATTERNS = [
    path("auth/login/", obtain_auth_token, name="auth_login"),
    path("auth/register/", CustomerRegistrationView.as_view(), name="auth_registration")
]

urlpatterns = [
    *AUTHENTICATION_URL_PATTERNS,
]
