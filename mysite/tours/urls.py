from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('tour/<int:tour_id>/', views.tour_detail, name='tour_detail'), 
    path('order/<int:tour_id>/', views.order_tour, name='order_tour'),  
]
