from django.urls.converters import uuid
from drf_yasg.utils import APIView, status, swagger_auto_schema
from rest_framework import permissions
from rest_framework.compat import requests
from rest_framework.views import Response

from cores.constants import SwaggerTag
from transaction.serializers.virtual_account import CreateVirtualAccountRequestSerializer, PayVirtualAccountResponseSerializer, VirtualAccountSerializer, ListVirtualAccountResponseSerializer

from os import environ

TRANSACTION_SERVICE_URL = environ.get("TRANSACTION_SERVICE_HOST")

class ListCreateVirtualAccountView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        request_body=CreateVirtualAccountRequestSerializer(),
        responses={
            "201": VirtualAccountSerializer(),
        },
        tags=[SwaggerTag.VIRTUAL_ACCOUNT]
    )
    def post(self, request):
        virtual_account = requests.post(f"{TRANSACTION_SERVICE_URL}/virtual-account/", json={
            "userId": str(request.user.id),
            "title": request.data["title"],
            "description": request.data["description"],
            "amount": request.data["transaction_amount"],
        })
        
        return Response(
            virtual_account.json(),
            status=status.HTTP_201_CREATED
        )

    @swagger_auto_schema(
        responses={
            "200": ListVirtualAccountResponseSerializer()
        },
        tags=[SwaggerTag.VIRTUAL_ACCOUNT]
    )
    def get(self, request):
        virtual_accounts = requests.get(f"{TRANSACTION_SERVICE_URL}/virtual-account/account/{request.user.id}")

        return Response(
            virtual_accounts.json()
        )

class GetUpdateDeleteVirtualAccountView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        responses={
            "200": VirtualAccountSerializer()
        },
        tags=[SwaggerTag.VIRTUAL_ACCOUNT]
    )
    def get(self, request, virtual_account_id: str):
        virtual_account = requests.get(f"{TRANSACTION_SERVICE_URL}/virtual-account/{virtual_account_id}")

        return Response(virtual_account.json(), status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={
            "201": PayVirtualAccountResponseSerializer(),
        },
        tags=[SwaggerTag.VIRTUAL_ACCOUNT]
    )
    def put(self, request, virtual_account_id: str):
        virtual_account = requests.put(f"{TRANSACTION_SERVICE_URL}/virtual-account/{virtual_account_id}", json={
            "userId": str(request.user.id)
        })
        print(virtual_account.json())
        return Response(virtual_account.json(), status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        responses={
            "204": None
        },
        tags=[SwaggerTag.VIRTUAL_ACCOUNT]
    )
    def delete(self, request, virtual_account_id: str):
        virtual_account = requests.delete(f"{TRANSACTION_SERVICE_URL}/virtual-account/withdraw/{virtual_account_id}")

        return Response(status=status.HTTP_204_NO_CONTENT)
    
