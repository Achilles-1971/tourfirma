from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("orders/", views.order_list, name="order_list"),
    path("orders/cancel/<int:order_id>/", views.cancel_order, name="cancel_order"),
    path("orders/restore/<int:order_id>/", views.restore_order, name="restore_order"),
    path("tours/", views.tour_list, name="tour_list"),
    path("tours/<int:tour_id>/", views.tour_detail, name="tour_detail"),
    path("tours/order/<int:tour_id>/", views.order_tour, name="order_tour"),
    path("news/", views.news_list, name="news_list"),
    path("news/<int:news_id>/", views.news_detail, name="news_detail"),
    path('news/<int:news_id>/add_comment/', views.add_comment, name='add_comment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
