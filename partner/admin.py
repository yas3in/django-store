from django.contrib import admin
from django.contrib.admin import register
from partner.models import Partner, PartnerStock

@register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name']
    

@register(PartnerStock)
class PartnerStockAdmin(admin.ModelAdmin):
    list_display = ['partner', 'product', 'price']
