from django.urls.converters import uuid
from drf_yasg.utils import APIView, status, swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import Response

from cores.constants import SwaggerTag
from transaction.serializers.virtual_account import CreateVirtualAccountRequestSerializer, PayVirtualAccountResponseSerializer, VirtualAccountSerializer, ListVirtualAccountResponseSerializer


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
        pass

    @swagger_auto_schema(
        responses={
            "200": ListVirtualAccountResponseSerializer()
        },
        tags=[SwaggerTag.VIRTUAL_ACCOUNT]
    )
    def get(self, request):
        pass

class GetUpdateDeleteVirtualAccountView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        responses={
            "200": VirtualAccountSerializer()
        },
        tags=[SwaggerTag.VIRTUAL_ACCOUNT]
    )
    def get(self, request, virtual_account_id: uuid.UUID):
        return Response(status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={
            "201": PayVirtualAccountResponseSerializer(),
        },
        tags=[SwaggerTag.VIRTUAL_ACCOUNT]
    )
    def put(self, request):
        return Response(status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        responses={
            "204": None
        },
        tags=[SwaggerTag.VIRTUAL_ACCOUNT]
    )
    def delete(self, request):
        return Response(status=status.HTTP_204_NO_CONTENT)
    
