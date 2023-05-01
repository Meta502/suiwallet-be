from rest_framework import serializers

from cores.constants import DecimalConstant

class CreateTransferRequestSerializer(serializers.Serializer):
    target_account_number=serializers.CharField()
    amount=serializers.DecimalField(max_digits=DecimalConstant.MAX_DIGITS, decimal_places=DecimalConstant.DECIMAL_PLACES)
    notes=serializers.CharField()

class CreateTransferResponseSerializer(serializers.Serializer):
    transaction_id=serializers.CharField()
    target_account_number=serializers.CharField()
    amount=serializers.DecimalField(max_digits=DecimalConstant.MAX_DIGITS, decimal_places=DecimalConstant.DECIMAL_PLACES)
    notes=serializers.CharField()
    message=serializers.CharField()
