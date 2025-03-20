from django.urls import path

from apps.wallet.view.front import TransferTransactionApiView


urlpatterns = [
    path("transfer/", TransferTransactionApiView.as_view(), name="transfer")
]