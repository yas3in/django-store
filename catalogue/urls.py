from webdesign.urls import path
from catalogue.views import products, product_detail


urlpatterns = [
    path('', products, name="products"),
    path('product-detail/<int:id>', product_detail, name="product-detail")
]
