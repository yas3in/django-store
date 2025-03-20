from rest_framework import serializers
from rest_framework.generics import ValidationError
from rest_framework.response import Response

from apps.wallet.models import Transaction
from django.contrib.auth.models import User

from apps.wallet.utils import  CreateTransaction


class CreateTransferTransactionSerializer(serializers.ModelSerializer):
    received_transaction = serializers.CharField()
    amount = serializers.IntegerField()

    class Meta:
        model = Transaction
        fields = ("amount", "received_transaction")
        
    def create(self, validated_data):
        receiver_instance = CreateTransaction.transfer(
            receiver=validated_data["received_transaction"], amount=validated_data["amount"], sender=self.context["request"].user
            )
        if receiver_instance is None:
            return ValidationError("transaction has a error please try again later")
        validated_data.pop("received_transaction")
        sender_transaction = super().create(validated_data)
        print(sender_transaction)
        return sender_transaction
    
    def validate_amount(self, attr):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user

        if Transaction.balance(user)["balance"] <= 0 or attr <= 0:
            raise ValidationError("you can't transfer this value",)
        return attr
