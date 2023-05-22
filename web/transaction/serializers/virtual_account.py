from rest_framework import serializers

from cores.constants import DecimalConstant

class ItemSerializer(serializers.Serializer):
    name = serializers.CharField()
    amount = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=DecimalConstant.MAX_DIGITS, decimal_places=DecimalConstant.DECIMAL_PLACES)
    notes = serializers.CharField(allow_blank=True, allow_null=True)

class CreateVirtualAccountRequestSerializer(serializers.Serializer):
    title = serializers.CharField(allow_blank=True, allow_null=True)
    description = serializers.CharField(allow_blank=True, allow_null=True)
    transaction_amount = serializers.DecimalField(max_digits=DecimalConstant.MAX_DIGITS, decimal_places=DecimalConstant.DECIMAL_PLACES)

class VirtualAccountSerializer(serializers.Serializer):
    title = serializers.CharField(allow_blank=True, allow_null=True)
    description = serializers.CharField(allow_blank=True, allow_null=True)
    items = serializers.ListField(child=ItemSerializer(), default=list)
    transaction_amount = serializers.DecimalField(max_digits=DecimalConstant.MAX_DIGITS, decimal_places=DecimalConstant.DECIMAL_PLACES)
    recurring = serializers.BooleanField(default=False)
    payment_code = serializers.CharField()

class ListVirtualAccountResponseSerializer(serializers.Serializer):
    items = serializers.ListField(
        child=VirtualAccountSerializer(),
    )

class PayVirtualAccountResponseSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    payment_id = serializers.UUIDField() 
    remaining_balance = serializers.DecimalField(
        max_digits=DecimalConstant.MAX_DIGITS,
        decimal_places=DecimalConstant.DECIMAL_PLACES,
    )
    amount_deducted = serializers.DecimalField(
        max_digits=DecimalConstant.MAX_DIGITS,
        decimal_places=DecimalConstant.DECIMAL_PLACES,
    )

