from django.contrib import admin

from django.contrib.admin import register

from catalouge.models import Brand, Category, Product, ProductAttribute, ProductType, ProductAttributeValue



class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute



@register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "parent")



@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent")



@register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "title", "upc", "product_type", "is_active", "description", "category", "brand"
        )
    search_fields = ("title", "brand", "product_type")
    list_editable = ("is_active",)
    
    
    

@register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ("title", "product_type", "attribute_type")
    


@register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    inlines = [ProductAttributeInline]



@register(ProductAttributeValue)
class ProductAttributeValueAdmin(admin.ModelAdmin):
    list_display = ("product", "value", "attribute")
