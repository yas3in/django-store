from django.db import models


class ProductType(models.Model):
    title = models.CharField(max_length=32, blank=True, null=True)
    description = models.TextField(blank=True)
    
    
    def __str__(self):
        return self.title

    
    
class Category(models.Model):
    name = models.CharField(max_length=32)
    # فیلد جدول خود را با سلف به همان جدول کلید خارجی میکنیم
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name="children", null=True, blank=True)


    def __str__(self):
        return self.name
    

class Brand(models.Model):
    name = models.CharField(max_length=32)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name="children", null=True, blank=True)


    def __str__(self):
        return self.name
    
  
    
class ProductAttribute(models.Model):
    INTEGER = 1
    STRING = 2
    FLOAT = 3
    
    ATTRIBUTE_TYPES_FILTERS = (
        (INTEGER, "integer"),
        (STRING, "string"),
        (FLOAT, "float")
    )
    
    title = models.CharField(max_length=255)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name="products")
    attribute_type = models.PositiveSmallIntegerField(default=INTEGER, choices=ATTRIBUTE_TYPES_FILTERS)
    
    
    def __str__(self):
        return self.title
    
 
class Product(models.Model):
    title = models.CharField(max_length=255)
    upc = models.BigIntegerField(unique=True)
    description = models.TextField(blank=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT)
    category = models.ForeignKey(Category , on_delete=models.CASCADE, related_name="products", blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="products", blank=True, null=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.title



class ProductAttributeValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="attribute_value")
    value = models.CharField(max_length=40)
    attribute = models.ForeignKey(ProductAttribute, on_delete=models.PROTECT, related_name="value")
    
    
    def __str__(self):
        return self.product