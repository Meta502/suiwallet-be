from dataclasses import dataclass
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

@dataclass
class RegisterCustomerDataClass:
    username: str
    email: str

class RegisterCustomerService:
    @classmethod
    def run(cls, username: str, password: str, email: str) -> RegisterCustomerDataClass:
        user = User.objects.create_user(
            username,
            email,
            password,
        )

        return RegisterCustomerDataClass(
            username=user.username,
            email=user.email,
        )
