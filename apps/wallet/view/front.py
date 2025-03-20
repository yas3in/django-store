from django.http import HttpResponse
from apps.wallet.models import Transaction
from rest_framework.generics import CreateAPIView   

from rest_framework import status
from apps.wallet.serializer.front import CreateTransferTransactionSerializer
from django.contrib.auth.models import User
from apps.wallet.utils import CreateTransaction

class TransferTransactionApiView(CreateAPIView):
    serializer_class = CreateTransferTransactionSerializer
    queryset = Transaction

    def get_queryset(self):
        query = Transaction.objects.filter(user=self.request.user)
        return query

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, transaction_type="Transfer Sent")