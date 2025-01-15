from django.shortcuts import render, get_object_or_404
from .models import Tour, Order  # Импортируем модели

def home(request):
    return render(request, 'home.html')

# Список доступных туров
def tour_list(request):
    tours = Tour.objects.all()
    return render(request, 'tour_list.html', {'tours': tours})

# Детальная информация о туре
def tour_detail(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    return render(request, 'tour_detail.html', {'tour': tour})

# Список активных заказов
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

# Оформление заказа
def order_tour(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)

    if request.method == "POST":
        # Здесь можно добавить сохранение заказа
        return render(request, 'order_success.html', {'tour': tour})

    return render(request, 'order_tour.html', {'tour': tour})
