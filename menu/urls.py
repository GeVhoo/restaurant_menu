from django.urls import path

from . import views


app_name = 'menu'
urlpatterns = [
    path('', views.MenuView.as_view(), name='dishes'),
    path('order/', views.OrderView.as_view(), name='order'),
    path('api_info/', views.api_info, name='api_info')
]
