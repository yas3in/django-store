from webdesign.urls import path
from catalouge.views import products


urlpatterns = [
    path('products', products)
]
