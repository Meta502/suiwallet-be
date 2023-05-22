from dataclasses import dataclass

from rest_framework.compat import requests
from cores.models import SuiwalletUser
from customer.models import Customer, Address
from rest_framework.authtoken.models import Token
from os import environ

import datetime

TRANSACTION_SERVICE_URL = environ.get("TRANSACTION_SERVICE_HOST")

@dataclass
class RegisterCustomerDataClass:
    username: str
    email: str
    nik: str
    birth_date: datetime.date
    phone_number: str
    address: str
    postal_code: str

class RegisterCustomerService:
    @classmethod
    def run(cls, username: str, password: str, email: str, nik: str, birth_date: datetime.date, phone_number: str, address: str, postal_code: str) -> RegisterCustomerDataClass:
        user = SuiwalletUser.objects.create_user(
            username,
            email,
            password,
        )

        customer = Customer.objects.create(
            user = user,
            birth_date = birth_date,
            phone_number = phone_number,
            identification_number = nik
        )

        addressObj = Address.objects.create(
            customer = customer,
            address_text = address,
            postal_code = postal_code
        )

        requests.post(f"{TRANSACTION_SERVICE_URL}/account/{user.id}")

        return RegisterCustomerDataClass(
            username=user.username,
            email=user.email,
            nik=customer.identification_number,
            birth_date=customer.birth_date,
            phone_number=customer.phone_number,
            address=addressObj.address_text,
            postal_code=addressObj.postal_code
        )
