from rest_framework import serializers

from cores.constants import DecimalConstant

class CreateTransferRequestSerializer(serializers.Serializer):
    target_account=serializers.CharField()
    amount=serializers.DecimalField(max_digits=DecimalConstant.MAX_DIGITS, decimal_places=DecimalConstant.DECIMAL_PLACES)

class CreateTransferResponseSerializer(serializers.Serializer):
    transaction_id=serializers.CharField()
    amount=serializers.DecimalField(max_digits=DecimalConstant.MAX_DIGITS, decimal_places=DecimalConstant.DECIMAL_PLACES)
