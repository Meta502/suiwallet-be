from django.db import models

from rest_framework.serializers import ValidationError

from cores.models import SuiwalletUser

# Create your models here.
class Address(models.Model):
    customer = models.OneToOneField(
        "customer.Customer",
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="address",
    )
    address_text = models.CharField(max_length=1024)
    postal_code = models.CharField(max_length=16)
    

class Customer(models.Model):
    def validate_phone_number(self, value):
        if not re.match("^(^\+62|62|^08)(\d{3,4}-?){2}\d{3,4}$", value):
            raise ValidationError("Nomor telepon ini tidak valid")

    user = models.OneToOneField(
        SuiwalletUser,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="customer",
    )
    birth_date = models.DateTimeField()
    phone_number = models.CharField(max_length=64, validators=[validate_phone_number])
    identification_number = models.CharField(max_length=16)
