from drf_yasg.utils import APIView, swagger_auto_schema
from rest_framework import permissions, serializers
from rest_framework.authtoken.views import Response
from rest_framework.compat import requests
from rest_framework.exceptions import status
from cores.constants import SwaggerTag

from transaction.serializers.top_up import TopUpRequestSerializer, TopUpResponseSerializer

from os import environ

TRANSACTION_SERVICE_URL = environ.get("TRANSACTION_SERVICE_HOST")

class TopUpView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        request_body=TopUpRequestSerializer(),
        responses={
            "201": TopUpResponseSerializer(),
        },
        tags=[SwaggerTag.TOP_UP]
    )
    def post(self, request):
        top_up = requests.post(f"{TRANSACTION_SERVICE_URL}/top-up", json={
            "accountId": str(request.user.id),
            "amount": request.data["amount"],
        })

        return Response(
            top_up.json(),
            status=status.HTTP_201_CREATED,
        )


class PayTopUpView(APIView):
    @swagger_auto_schema()
    def put(self, request, top_up_id: str):
        top_up = requests.put(f"{TRANSACTION_SERVICE_URL}/top-up/{top_up_id}")

        return Response(
            top_up.json(),
            status=top_up.status_code
        )
    
