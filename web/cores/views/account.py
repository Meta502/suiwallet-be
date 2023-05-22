from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.authtoken.views import APIView, Response
from rest_framework.compat import requests

from os import environ

TRANSACTION_SERVICE_URL = environ.get("TRANSACTION_SERVICE_HOST")

class AccountView(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    @swagger_auto_schema()
    def get(self, request):
        api_request = requests.get(f"{TRANSACTION_SERVICE_URL}/account/{request.user.id}")
        
        return Response(api_request.json())
