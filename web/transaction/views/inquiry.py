from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
from rest_framework.renderers import serializers
from rest_framework.views import APIView, Response, status
from rest_framework import permissions

from cores.constants import SwaggerTag


class InquiryView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    class InquiryRequestSerializer(serializers.Serializer):
        start_date = serializers.DateTimeField(allow_null=True, default=timezone.now() - timezone.timedelta(days=7))
        end_date = serializers.DateTimeField(allow_null=True, default=timezone.now())
        filter_type = serializers.ChoiceField(choices=(
            ("all", "All"),
            ("top_up", "Top Up"),
            ("transfer", "Transfer"),
            ("virtual_account", "Virtual Account")
        ))

    @swagger_auto_schema(
        request_body=InquiryRequestSerializer(),
        responses={
            "200": None 
        },
        tags=[SwaggerTag.INQUIRY],
    )
    def post(self, request):
        return Response(status=status.HTTP_200_OK)

    
