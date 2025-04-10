from rest_framework import serializers
from rest_framework.generics import ValidationError

from apps.wallet.models import Transaction
from apps.wallet.utils import  CreateTransaction

from django.contrib.auth.models import User
from django.db.transaction import atomic

class CreateTransferTransactionSerializer(serializers.ModelSerializer):
    received_transaction = serializers.CharField()
    amount = serializers.IntegerField()

    class Meta:
        model = Transaction
        fields = ("amount", "received_transaction")
        
    def create(self, validated_data):
        """
        Separate the recipient and perform the transfer transaction.
        """
        try:
            with atomic():
                amount = self.validate_amount(validated_data["amount"])
                receiver_instance = CreateTransaction.transfer(
                    receiver=validated_data["received_transaction"], amount=amount, sender=self.context["request"].user
                    )
                receiver_instance = self.validate_received_transaction(receiver_instance)
                validated_data.pop("received_transaction")
                sender_transaction = super().create(validated_data)
        except:
            return ValidationError("error in transaction")
        else:
            return sender_transaction
    
    def validate_amount(self, attr):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user

        if Transaction.balance(user)["balance"] <= 0 or attr <= 0:
            raise ValidationError("you can't transfer this value",)
        return attr

    def validate_received_transaction(self, attr):
        try:
            user = User.objects.get(username=attr)
        except:
            return ValidationError("user is not valid")
        else:
            return user