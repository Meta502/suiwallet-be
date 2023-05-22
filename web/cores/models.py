from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import uuid

class SuiwalletUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

