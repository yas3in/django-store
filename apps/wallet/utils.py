from django.contrib.auth.models import User
from rest_framework.generics import ValidationError
from apps.wallet.tools.decorators import is_uservalid
from apps.wallet.models import Transaction, TransferTransaction, UserBalance
from django.db.transaction import atomic


class CreateTransaction:
    def __init__(self, sender, receiver, amount):
        self.amount = amount
        self.sender = sender
        self.receiver = receiver
            
    @classmethod
    def calcuate_balance(self, sender, receiver):
        try:
            sender = User.objects.get(username=sender)
        except:
            raise "error in sender in utils"
            
        try:
            receiver = User.objects.get(username=receiver)
        except:
            raise "error in sender in utils"
            UserBalance.create_instance_in_table(sender)
            UserBalance.create_instance_in_table(receiver)
        
            raise "error in calculate_balance"
 
    @classmethod
    def transfer(cls, receiver, sender, amount):
        with atomic():
            return cls.calcuate_balance(sender=sender, receiver=receiver)
        return receiver_instance
