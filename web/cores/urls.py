from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from cores.views.account import AccountView

from cores.views.authentication import CustomerRegistrationView, CustomerValidationView

AUTHENTICATION_URL_PATTERNS = [
    path("auth/login/", obtain_auth_token, name="auth_login"),
    path("auth/register/", CustomerRegistrationView.as_view(), name="auth_registration"),
    path("auth/validate/", CustomerValidationView.as_view(), name="auth_validate")
]

ACCOUNT_URL_PATTERNS = [
    path("account/", AccountView.as_view(), name="account_get")
]

urlpatterns = [
    *AUTHENTICATION_URL_PATTERNS,
    *ACCOUNT_URL_PATTERNS,
]
