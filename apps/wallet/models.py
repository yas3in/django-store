from django.db import models
from django.conf import settings

from django.db.models import Sum, Q
from django.db.models.functions import Coalesce 


class Transaction(models.Model):
    TRANSACTION_TYPE_CHICES = (
        ("Charge", "Charge"),
        ("Purchase", "Purchase"),
        ("Transfer received", "Transfer received"),
        ("Transfer Sent", "Transfer Sent")
    )
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="transactions", on_delete=models.RESTRICT)
    transaction_type = models.CharField(choices=TRANSACTION_TYPE_CHICES, max_length=152)
    amount = models.BigIntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    
    @classmethod
    def balance(cls, user):
        """
        transaction it`s related name`s Transction model to User model
        
        """
        # Adad fard baraye jam va ada zoj baraye menha az balance hast
        positive_transaction = Sum("amount", filter=Q(transaction_type__in=["Charge", "Transfer received"]))
        negative_transaction = Sum("amount", filter=Q(transaction_type__in=["Transfer Sent", "Purchase"]))
        user_balance = user.transactions.all().aggregate(
            balance=Coalesce(positive_transaction, 0) - Coalesce(negative_transaction, 0)
        )
        
        return user_balance
    
    def __str__(self) -> str:
        return f"{self.user} - {self.get_transaction_type_display()} - {self.amount}"


class UserBalance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="userbalance", on_delete=models.RESTRICT)
    balance = models.BigIntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.user} - {self.balance} - {self.created_time}"
    
    @classmethod
    def create_instance_in_table(cls, user):
        instance = cls.objects.create(user=user, balance=Transaction.balance(user)['balance'])
        return instance
        
    @classmethod
    def create_record_in_table(cls):
        for user in settings.AUTH_USER_MODEL.objects.all():
            record = cls.create_instance_in_table(user)
            

class TransferTransaction(models.Model):
    sender_transaction = models.ForeignKey(Transaction, related_name="sender_transaction", on_delete=models.RESTRICT)
    receiver_transaction = models.ForeignKey(Transaction, related_name="received_transaction", on_delete=models.RESTRICT)
    
    def __str__(self):
        return f"{self.sender_transaction} to {self.received_transaction}"
