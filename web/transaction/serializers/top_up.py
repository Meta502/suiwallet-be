from rest_framework import serializers

from cores.constants import DecimalConstant
from transaction.constants import PAYMENT_METHOD_TYPE_CHOICES

class TopUpRequestSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=DecimalConstant.MAX_DIGITS, decimal_places=DecimalConstant.DECIMAL_PLACES)
    payment_method = serializers.ChoiceField(choices=PAYMENT_METHOD_TYPE_CHOICES)
    

class TopUpResponseSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    payment_code = serializers.CharField()
    amount = serializers.DecimalField(
        max_digits=DecimalConstant.MAX_DIGITS,
        decimal_places=DecimalConstant.DECIMAL_PLACES,
    )
    platform_fee = serializers.DecimalField(
        max_digits=DecimalConstant.MAX_DIGITS,
        decimal_places=DecimalConstant.DECIMAL_PLACES,
    )

