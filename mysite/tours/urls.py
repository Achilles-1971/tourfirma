from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("orders/", views.order_list, name="order_list"),
    path("orders/cancel/<int:order_id>/", views.cancel_order, name="cancel_order"),  # Добавьте этот маршрут
    path("tours/", views.tour_list, name="tour_list"),
    path("tours/<int:tour_id>/", views.tour_detail, name="tour_detail"),
    path("tours/order/<int:tour_id>/", views.order_tour, name="order_tour"),
    path("orders/restore/<int:order_id>/", views.restore_order, name="restore_order"),

]
