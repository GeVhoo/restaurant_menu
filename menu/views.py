from django.shortcuts import render, HttpResponseRedirect
from django.views import View

from .models import Dish


class MenuView(View):
    """Предоставляет пользователю меню всех блюд для заказа."""
    def get(self, request):
        """Выводит меню всех блюд на начальной странице."""
        dishes = Dish.objects.order_by('category')
        return render(request, 'menu/index.html', {'dishes': dishes})

    def post(self, request):
        """Получает данные из формы и отправляет на страницу заказа."""
        request.session['dishes'] = request.POST.getlist('selected_id')
        return HttpResponseRedirect('/order/')


class OrderView(View):
    """Предоставляет информацию о заказе."""
    def get(self, request):
        """Обрабатывает данные из формы меню и выводит заказе."""
        dishes_id = _get_list_dishes_id(request.session.get('dishes'))
        if dishes_id is None:
            dishes = dishes_id
        else:
            dishes = Dish.objects.filter(id__in=dishes_id)
        order_price = _get_order_price(dishes)
        return render(request, 'menu/order.html',
                      {'dishes': dishes, 'order_price': order_price})


def api_info(request):
    """Страница документации API ресторана."""
    return render(request, 'menu/api_info.html')


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
