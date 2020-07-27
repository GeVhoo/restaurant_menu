from django.urls import path

from . import views


app_name = 'menu'
urlpatterns = [
    path('', views.menu, name='dishes'),
    path('order/', views.order, name='order'),
]
