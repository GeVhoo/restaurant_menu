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
    dishes_id = _get_dish_id(request.session.get('dishes'))
    if dishes_id is None:
        dishes = dishes_id
    else:
        dishes = Dish.objects.filter(id__in=dishes_id)
    return render(request, 'menu/order.html', {'dishes': dishes})


def _get_dish_id(list_id):
    if list_id:
        return list(map(int, list_id))
    return None
