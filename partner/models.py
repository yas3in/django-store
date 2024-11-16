from django.db import models

from catalogue.models import Product


class Partner(models.Model):
    name = models.CharField(max_length=48)
    
    
    def __str__(self):
        return f"{self.name}"
    
    
class PartnerStock(models.Model):
    partner = models.ForeignKey(Partner, related_name="partner", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="partner_product", on_delete=models.CASCADE)
    price = models.PositiveBigIntegerField(default=0)
    
    
    def __str__(self):
        return f"{self.partner} - {self.product} - {self.price}"
    
    