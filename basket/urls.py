from django.urls import path, include
from basket.views import add_to_basket


urlpatterns = [
    path('add/',add_to_basket, name="add-to-basket")
]
