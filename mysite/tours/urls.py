from django.urls import path
from .views import home, tour_list, tour_detail, order_list, order_tour

urlpatterns = [
    path('', home, name='home'),
    path('tours/', tour_list, name='tour_list'),
    path('tours/<int:tour_id>/', tour_detail, name='tour_detail'),
    path('orders/', order_list, name='order_list'),
    path('orders/<int:tour_id>/', order_tour, name='order_tour'),
    
]
