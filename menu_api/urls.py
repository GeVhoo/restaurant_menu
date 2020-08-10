from django.urls import path

from . import views


app_name = 'menu_api'
urlpatterns = [
    path('menu/', views.MenuListView.as_view(), name='menu_list'),
    path('dish/add/', views.DishAddView.as_view(), name='dish_add'),
]
