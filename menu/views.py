from django.shortcuts import render, HttpResponseRedirect

from .models import Dish


def menu(request):
    """Предоставляет пользователю меню всех блюд для заказа."""
    dishes = Dish.objects.order_by('category')
    if request.POST:
        request.session['dishes'] = request.POST.getlist('selected_id')
        return HttpResponseRedirect('/order/')
    return render(request, 'menu/index.html', {'dishes': dishes})


def order(request):
    """Выводит информацию о заказе."""
    dishes_id = _get_list_dishes_id(request.session.get('dishes'))
    if dishes_id is None:
        dishes = dishes_id
    else:
        dishes = Dish.objects.filter(id__in=dishes_id)
    order_price = _get_order_price(dishes)
    return render(request, 'menu/order.html',
                  {'dishes': dishes, 'order_price': order_price})


def _get_list_dishes_id(list_id):
    if list_id:
        return list(map(int, list_id))
    return None


def _get_order_price(items):
    order_price = 0
    if items:
        for item in items:
            order_price += item.price
    return order_price
