from django.urls.converters import uuid
from django.utils import timezone
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView, Response, status
from rest_framework import permissions
import requests

from cores.constants import SwaggerTag
from transaction.serializers.inquiry import InquiryRequestSerializer, InquiryResponseSerializer, TransactionSerializer
from os import environ

TRANSACTION_SERVICE_URL = environ.get("TRANSACTION_SERVICE_HOST")

class ListInquiryView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "start_date", openapi.IN_QUERY, type=openapi.TYPE_STRING,
                description="Start date range in ISO datetime string"
            ),
            openapi.Parameter(
                "end_date", openapi.IN_QUERY, type=openapi.TYPE_STRING,
                description="End date range in ISO datetime string"
            ),
            openapi.Parameter(
                "filter_type", openapi.IN_QUERY, type=openapi.TYPE_STRING,
                description="Filter by transaction type. Available choices: 'all', 'virtual_account', 'top_up', 'transfer'"
            )
        ],
        responses={
            "200": InquiryResponseSerializer(),
        },
        tags=[SwaggerTag.INQUIRY],
    )
    def get(self, request):
        api_request = requests.get(f"{TRANSACTION_SERVICE_URL}/inquiry/{request.user.id}")
        
        data = api_request.json()
        print(data)
        print(request.user.id)

        return Response(data, status=status.HTTP_200_OK)

class GetInquiryView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    @swagger_auto_schema(
        responses={
            "200": TransactionSerializer()
        },
        tags=[SwaggerTag.INQUIRY],
    )
    def get(self, request, transaction_id: uuid.UUID):
        print(request.user)

        return Response()

