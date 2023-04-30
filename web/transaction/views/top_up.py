from drf_yasg.utils import APIView, swagger_auto_schema
from rest_framework import permissions, serializers
from cores.constants import SwaggerTag

from transaction.serializers.top_up import TopUpRequestSerializer, TopUpResponseSerializer


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
        pass
    
