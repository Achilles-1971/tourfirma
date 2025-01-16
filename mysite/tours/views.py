from django.shortcuts import render, get_object_or_404
from .models import Tour, Order

def home(request):
    return render(request, 'home.html')

def tour_list(request):
    tours = Tour.objects.all()
    return render(request, 'tour_list.html', {'tours': tours})

def tour_detail(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    return render(request, 'tour_detail.html', {'tour': tour})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

def active_orders(request):
    orders = Order.objects.filter(is_active=True) 
    return render(request, "orders/active_orders.html", {"orders": orders})

def order_tour(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    order = Order.objects.create(user=request.user, tour=tour, is_active=True)

    if request.method == "POST":
        return render(request, 'order_success.html', {'tour': tour})

    return render(request, 'order_success.html', {'tour': tour})



