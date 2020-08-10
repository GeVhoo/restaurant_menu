from rest_framework import generics
from rest_framework.permissions import BasePermission

from menu.models import Dish
from restaurant_menu.settings import API_TOKEN

from .serializers import DishAddSerializer, MenuListSerializer


class ApiUserPermission(BasePermission):
    """Изменяет BasePermission: доступ по токену."""
    def has_permission(self, request, view):
        return request.META['HTTP_API_TOKEN'] == API_TOKEN


class DishAddView(generics.CreateAPIView):
    """Представление для добавления блюда."""
    permission_classes = [ApiUserPermission]
    serializer_class = DishAddSerializer


class MenuListView(generics.ListAPIView):
    """Представление для получения меню блюд."""
    permission_classes = [ApiUserPermission]
    serializer_class = MenuListSerializer
    queryset = Dish.objects.all()
