from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import APIView, Response, status

from cores.serializers.authentication.registration import RegistrationRequestSerializer, RegistrationResponseSerializer
from cores.services.register_customer import RegisterCustomerService

class CustomerRegistrationView(APIView):
    permission_classes = [
        permissions.AllowAny,
    ]
    
    @swagger_auto_schema(
        request_body=RegistrationRequestSerializer(),
        responses={
            "201": RegistrationResponseSerializer(), 
        }
    )
    def post(self, request):
        serializer = RegistrationRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        registered_user = RegisterCustomerService.run(
            **serializer.data
        )

        return Response(
            RegistrationResponseSerializer(
                registered_user
            ).data,
            status=status.HTTP_201_CREATED
        )

class CustomerValidationView(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get(self, request):
        return Response({
            "id": str(request.user.id)
        })
