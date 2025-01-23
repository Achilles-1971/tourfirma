from django.shortcuts import render, get_object_or_404, redirect
from .models import Tour, Order
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from .models import News


def home(request):
    news = News.objects.all().order_by("-created_at")[:3]
    return render(request, "home.html", {"news": news})

def order_list(request):
    status_filter = request.GET.get("status")
    sort_by = request.GET.get("sort")
    orders = Order.objects.filter(user=request.user)

    if status_filter:
        orders = orders.filter(status=status_filter)

    if sort_by:
        if sort_by == "date_asc":
            orders = orders.order_by("order_date")
        elif sort_by == "date_desc":
            orders = orders.order_by("-order_date")
        elif sort_by == "price_asc":
            orders = orders.order_by("tour__price")
        elif sort_by == "price_desc":
            orders = orders.order_by("-tour__price")

    paginator = Paginator(orders, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "order_list.html", {"page_obj": page_obj})


from django.shortcuts import render
from .models import Tour


from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Tour


def tour_list(request):
    price_min = request.GET.get("price_min")
    price_max = request.GET.get("price_max")
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")


    tours = Tour.objects.all()

    if price_min:
        tours = tours.filter(price__gte=price_min)
    if price_max:
        tours = tours.filter(price__lte=price_max)
    if start_date:
        tours = tours.filter(start_date__gte=start_date)
    if end_date:
        tours = tours.filter(end_date__lte=end_date)

    paginator = Paginator(tours, 6)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "tour_list.html", {"page_obj": page_obj})


def tour_detail(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    return render(request, 'tour_detail.html', {'tour': tour})

@login_required
def order_tour(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == "POST":
        order = Order.objects.create(user=request.user, tour=tour)
        return render(request, "order_success.html", {"tour": tour})
    return render(request, "order_tour.html", {"tour": tour})


@login_required
def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if order.status == "active":
        order.status = "canceled"
        order.save()
    return redirect("order_list")


@login_required
def restore_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if order.status == "canceled":
        order.status = "active"
        order.save()
    return redirect("order_list")


def news_list(request):
    news = News.objects.all().order_by("-created_at")
    return render(request, "news_list.html", {"news": news})


def news_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    return render(request, "news_details.html", {"news": news})
