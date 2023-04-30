from django.utils import timezone
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.renderers import serializers
from rest_framework.serializers import ListSerializer
from rest_framework.views import APIView, Response, status
from rest_framework import permissions

from cores.constants import TRANSACTION_TYPE_CHOICES, DecimalConstant, SwaggerTag


class InquiryView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    class InquiryRequestSerializer(serializers.Serializer):
        start_date = serializers.DateTimeField(allow_null=True, default=timezone.now() - timezone.timedelta(days=7))
        end_date = serializers.DateTimeField(allow_null=True, default=timezone.now())
        filter_type = serializers.ChoiceField(
            choices=TRANSACTION_TYPE_CHOICES
        )

    class InquiryResponseSerializer(serializers.Serializer):
        class TransactionSerializer(serializers.Serializer):
            id = serializers.UUIDField()
            transaction_date = serializers.DateTimeField()
            amount = serializers.DecimalField(
                max_digits=DecimalConstant.MAX_DIGITS, 
                decimal_places=DecimalConstant.DECIMAL_PLACES
            )
        
        items = ListSerializer(
            child=TransactionSerializer()
        )

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
        return Response(status=status.HTTP_200_OK)

