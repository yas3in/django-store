from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def first_blog(request):
    text = """
    Hello! this is for blog in first django web. thank you.
    """
    return HttpResponse(text)    


def post_pages(request):
    return HttpResponse("Blog pages: ")


# #sum numbers in url
# def sum_numbers_in_url(request, number):
#     #The number argument is the same variable that we took(use) in path
#     numbers = str(number.replace("-", " "))
#     numbers = numbers.split(" ")
#     new_list = []
#     for number in numbers:
#         new_list.append(int(number))
#     sum = new_list[0] + new_list[1]
#     return HttpResponse(f" sum : {sum}")


def filter_post_city_list(request, city_name):
    city_list = ['tehran', 'shiraz', 'bandar-abbas']
    if city_name in city_list:
        return HttpResponse(f"shared posts from {city_name}")
    
    return HttpResponse("city noy founded")
    