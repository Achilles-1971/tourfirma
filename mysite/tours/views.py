from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, Tour

def home(request):
    tours = Tour.objects.all()  # Получаем все туры из базы данных
    return render(request, 'home.html', {'tours': tours})

def tour_detail(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id)  # Получаем тур по ID
    return render(request, 'tour_detail.html', {'tour': tour})

@login_required
def order_tour(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id)
    if request.method == 'POST':
        order = Order(user=request.user, tour=tour)
        order.save()  # Сохраняем заказ в базе данных
        return redirect('order_success')  # Перенаправляем на страницу с подтверждением

    return render(request, 'order_tour.html', {'tour': tour})