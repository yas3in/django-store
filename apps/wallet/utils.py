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
    def receiver(cls, receiver, amount):
        try:
            user = User.objects.get(username=receiver)
        except:
            raise "error in receiver"
        
        else:
            instance = Transaction.objects.create(
                user=user, amount=amount, transaction_type="Transfer received"
            )
            return instance
            
    @classmethod
    def calcuate_balance(self, sender, receiver):
        try:
            sender = User.objects.get(username=sender)
            receiver = User.objects.get(username=receiver)
            sender_transaction = UserBalance.create_instance_in_table(sender)
            receiver_transaction = UserBalance.create_instance_in_table(receiver)
        except:
            raise "error in calculate_balance"
        
    # @classmethod
    # def user_transfer(cls, sender, receiver, amount:int):
    #     check = Transaction.balance(sender)
    #     if check["balance"] < amount:
    #         return "You can`t transfer, because your amount not enough"
        
    #     with atomic():
    #         sender_transaction = Transaction.objects.create(
    #             user=sender, amount=amount, transaction_type=Transaction.TRANSFER_SENT
    #         )
            
    #         receiver_transaction = Transaction.objects.create(
    #             user=receiver, amount=amount, transaction_type=Transaction.TRANSFER_RECEIVED
    #         )
            
    #         instance = cls.objects.create(
    #             sender_transaction=sender_transaction, receiver_transaction=receiver_transaction
    #         )
        
    #     return instance
    
    @classmethod
    def transfer(cls, receiver, sender, amount):
        with atomic():
            receiver_instance = cls.receiver(receiver=receiver, amount=amount)
            if receiver_instance is not None:
                cls.calcuate_balance(sender=sender, receiver=receiver)
            else:
                raise "error in atomic transaction"
        return receiver_instance
