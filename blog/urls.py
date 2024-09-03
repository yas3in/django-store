from webdesign.urls import path
from blog.views import post_pages, filter_post_city_list
from django.urls import re_path


urlpatterns = [
    path('list/', post_pages),
    #get a number for show in url
    #variable use to path in <> and can use thi varibale in function
    # path('sum/<slug:number>/', sum_numbers_in_url),
    re_path(r'city-list/(?P<city_name>[\w-]+)/', filter_post_city_list)
    
]