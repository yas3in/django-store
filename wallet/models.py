from django.db import models
from blog.models import User
from django.db.models import Sum, Count, Q
from django.db.models.functions import Coalesce


class Transaction(models.Model):
    CHARGE = 1
    PURCHASE = 2
    TRANSFER_RECEIVED = 3
    TRANSFER_SENT = 4
    
    TRANSACTION_TYPE_CHICES = (
        (CHARGE, "Charge"),
        (PURCHASE, "Purchase"),
        (TRANSFER_RECEIVED, "Transfer received"),
        (TRANSFER_SENT, "Transfer Sent")
    )
    
    user = models.ForeignKey(User, related_name="transactions", on_delete=models.RESTRICT)
    transaction_type = models.PositiveSmallIntegerField(choices=TRANSACTION_TYPE_CHICES)
    amount = models.BigIntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    
    @classmethod
    def balance(cls, user):
        """
        transaction it`s related name`s Transction model to User model
        
        """
        # Adad fard baraye jam va ada zoj baraye menha az balance hast
        positive_transaction = Sum("amount", filter=Q(transaction_type__in=[1, 3]))
        
        negative_transaction = Sum("amount", filter=Q(transaction_type__in=[2, 4]))
        
        user_balance = user.transactions.all().aggregate(
            balance=Coalesce(positive_transaction, 0) - Coalesce(negative_transaction, 0)
        )
        
        return user_balance
    
    
    def __str__(self) -> str:
        return f"{self.user} - {self.get_transaction_type_display()} - {self.amount}"



class UserBalance(models.Model):
    user = models.ForeignKey(User, related_name="userbalance", on_delete=models.RESTRICT)
    balance = models.BigIntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return f"{self.user} - {self.balance} - {self.created_time}"
    
    
    @classmethod
    def create_instance_in_table(cls, user):
        instance = cls.objects.create(user=user, balance=Transaction.balance['balance'])
        return instance
        
        
        
    
    @classmethod
    def create_record_in_table(cls):
        for user in User.objects.all():
            record = cls.create_instance_in_table(user)
            
        
class TransferTransaction(models.Model):
    sender_transaction = models.ForeignKey(Transaction, related_name="sender_transaction", on_delete=models.RESTRICT)
    receiver_transaction = models.ForeignKey(Transaction, related_name="received_transaction", on_delete=models.RESTRICT)
    
    
    def __str__(self):
        return f"{self.sender_transaction} to {self.received_transaction}"
    
    
    @classmethod
    def user_transfer(cls, sender, receiver, amount):
        if Transaction.balance(sender) < amount:
            return "You can`t transfer, because your amount not enough"
        
        sender_transaction = Transaction.objects.create(
            user=sender, amount=amount, transaction_type=Transaction.TRANSFER_SENT
        )
        
        receiver_transaction = Transaction.objects.create(
            user=receiver, amount=amount, transaction_type=Transaction.TRANSFER_RECEIVED
        )
        
        instance = cls.objects.create(
            sender_transaction=sender_transaction, receiver_transaction=receiver_transaction
        )
        
        return instance