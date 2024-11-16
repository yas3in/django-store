from webdesign.urls import path
from catalogue.views import products


urlpatterns = [
    path('products', products)
]
