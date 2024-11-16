from django.db import models
from django.contrib.auth.models import User
from catalogue.models import Product

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="basket")
    created_time = models.DateTimeField(auto_now_add=True)


class BasketLine(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name="lines")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="lines")
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f"{self.basket}"