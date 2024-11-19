from webdesign.urls import path
from catalogue.views import products, product_detail
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', products, name="products"),
    path('product-detail/<int:id>', product_detail, name="product-detail")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
