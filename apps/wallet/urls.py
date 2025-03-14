from django.urls import path
from apps.wallet.views import show_users


urlpatterns = [
    path('users-amount', show_users)
]

