from webdesign.urls import path
from wallet.views import show_users


urlpatterns = [
    path('users-amount', show_users)
]

