from django.db import models
from blog.models import User
from django.db.models import Sum, Count, Q
from django.db.models.functions import Coalesce


class Transaction(models.Model):
    CHARGE = 1
    PURCHASE = 2
    TRANSFER = 3
    
    TRANSACTION_TYPE_CHICES = (
        (CHARGE, "Charge"),
        (PURCHASE, "Purchase"),
        (TRANSFER, "Transfer")
    )
    
    user = models.ForeignKey(User, related_name="transactions", on_delete=models.RESTRICT)
    transaction_type = models.PositiveSmallIntegerField(choices=TRANSACTION_TYPE_CHICES)
    amount = models.BigIntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return f"{self.user} - {self.get_transaction_type_display()} - {self.amount}"



class UserBalance(models.Model):
    user = models.ForeignKey(User, related_name="userbalance", on_delete=models.RESTRICT)
    balance = models.BigIntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return f"{self.user} - {self.balance} - {self.created_time}"
    
    
    @classmethod
    def created_instance(cls, user):
        """
        transaction its related name`s Transction model to User model
        
        """
        
        positive_transaction = Sum("amount", filter=Q(transaction_type=1))
        
        negative_transaction = Sum("amount", filter=Q(transaction_type__in=[2, 3]))
        
        user_balance = user.transactions.all().aggregate(
            balance=Coalesce(positive_transaction, 0) - Coalesce(negative_transaction, 0)
        )
        
        ins = cls.objects.create(user=user, balance=user_balance['balance'])
        return ins
        
        
        
    
    @classmethod
    def create_record_balance(cls):
        for user in User.objects.all():
            r = cls.created_instance(user)
            print(r)
