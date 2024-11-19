from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from basket.models import Basket


@require_POST
def add_to_basket(request):
    response = HttpResponseRedirect(request.POST.get('next', '/'))
    basket_id = request.COOKIES.get("basket_id", None)
    if basket_id is None:
        basket = Basket.objects.create()
        if request.user.is_authenticated:
            basket.user = request.user
            basket.save()
        response.set_cookie('basket_id', basket.id)
        print(response)
    return response
