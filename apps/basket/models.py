from django.db import models
from apps.accounts.models import CustomUser
from apps.catalogue.models import Product
from django.http import Http404


class Basket(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="basket", null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'

    def add(self, product, qty=1):
        
        if self.lines.filter(product=product).exists():
           product_line = self.lines.filter(product=product).first()
           product_line.quantity += qty
           product_line.save()
        else:
            product_line = self.lines.create(product=product, quantity=qty)
        return product_line

    def authenticated(self, user):
        if user.is_authenticated:
            if self.user is not None and self.user != user:
                return False  
            
            if self.user is None:    
                self.user = user
                self.save()     
                
        elif self.user is not None:
            return False
        return True

    @classmethod
    def get_basket(cls, basket_id):
        if basket_id is None:
            basket = cls.objects.create()
        else:
            try:
                basket = cls.objects.get(id=basket_id)
            except cls.DoesNotExist:
                basket = None
        return basket


class BasketLine(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name="lines")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="lines")
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f"{self.basket}"