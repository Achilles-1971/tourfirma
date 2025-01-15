from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tours/', views.tour_list, name='tour_list'),  # Список всех туров
    path('tours/<int:tour_id>/', views.tour_detail, name='tour_detail'),  # Детали тура
    path('orders/', views.order_list, name='order_list'),  # Список заказов
    path('orders/<int:tour_id>/', views.order_tour, name='order_tour'),  # Заказ тура
]
