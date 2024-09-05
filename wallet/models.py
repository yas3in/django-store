from django.db import models
from blog.models import User


class Transaction(models.Model):
    CHARGE = 1
    PURCHASE = 2
    TRANSFER = 3
    
    TRANSACTION_TYPE_CHICES = (
        (CHARGE, "Charge"),
        (PURCHASE, "Purchase"),
        (TRANSFER, "Transfer")
    )
    
    user = models.ForeignKey(User, related_name="transaction_user", on_delete=models.RESTRICT)
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
