from webdesign.urls import path
from blog.views import post_blog, filter_post_city_list, blogs
from django.urls import re_path


urlpatterns = [
    path("", blogs),
    path('list/', post_blog),
    re_path(r'city-list/(?P<city_name>[\w-]+)/', filter_post_city_list)
]