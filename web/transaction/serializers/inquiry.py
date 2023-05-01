from rest_framework import serializers
from django.utils import timezone

from cores.constants import TRANSACTION_TYPE_CHOICES, DecimalConstant


class TransactionSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    transaction_date = serializers.DateTimeField()
    amount = serializers.DecimalField(
        max_digits=DecimalConstant.MAX_DIGITS, 
        decimal_places=DecimalConstant.DECIMAL_PLACES
    )

class InquiryRequestSerializer(serializers.Serializer):
    start_date = serializers.DateTimeField(allow_null=True, default=timezone.now() - timezone.timedelta(days=7))
    end_date = serializers.DateTimeField(allow_null=True, default=timezone.now())
    filter_type = serializers.ChoiceField(
        choices=TRANSACTION_TYPE_CHOICES
    )

class InquiryResponseSerializer(serializers.Serializer): 
    items = serializers.ListSerializer(
        child=TransactionSerializer()
    )
