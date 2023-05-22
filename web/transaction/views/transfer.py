from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.authtoken.views import APIView, Response
from rest_framework.compat import requests

from cores.constants import SwaggerTag
from transaction.serializers.transfer import CreateTransferRequestSerializer, CreateTransferResponseSerializer

from os import environ
TRANSACTION_SERVICE_URL = environ.get("TRANSACTION_SERVICE_HOST")

class TransferView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        request_body=CreateTransferRequestSerializer(),
        responses={
            "201": CreateTransferResponseSerializer(),
        },
        tags=[SwaggerTag.TRANSFER]
    )
    def post(self, request):
        api_request = requests.post(f"{TRANSACTION_SERVICE_URL}/transfer", json={
            "sourceId": str(request.user.id),
            "targetId": request.data["target_account"],
            "amount": request.data["amount"],
        })

        return Response(api_request.json(), status=api_request.status_code)
