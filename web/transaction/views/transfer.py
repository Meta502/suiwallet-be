from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.authtoken.views import APIView

from cores.constants import SwaggerTag
from transaction.serializers.transfer import CreateTransferRequestSerializer, CreateTransferResponseSerializer


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
        pass
