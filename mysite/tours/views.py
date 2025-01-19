from django.shortcuts import render, get_object_or_404
from .models import Tour, Order
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def home(request):
    return render(request, "home.html")


def order_list(request):
    status_filter = request.GET.get("status")
    sort_by = request.GET.get("sort")

    orders = Order.objects.all()

    if status_filter:
        if status_filter == "active":
            orders = orders.filter(is_active=True)
        elif status_filter == "completed":
            orders = orders.filter(is_active=False)

    if sort_by:
        if sort_by == "date_asc":
            orders = orders.order_by("order_date")
        elif sort_by == "date_desc":
            orders = orders.order_by("-order_date")
        elif sort_by == "price_asc":
            orders = orders.order_by("tour__price")
        elif sort_by == "price_desc":
            orders = orders.order_by("-tour__price")

    return render(request, "order_list.html", {"orders": orders})



def tour_list(request):
    tours = Tour.objects.all()
    return render(request, "tour_list.html", {"tours": tours})


def tour_detail(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    return render(request, "tour_detail.html", {"tour": tour})


@login_required
def order_tour(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == "POST":
        order = Order.objects.create(user=request.user, tour=tour)
        return render(request, "order_success.html", {"tour": tour})
    return render(request, "order_tour.html", {"tour": tour})
