# tours/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Tour, Order, News, Comment
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def home(request):
    sort_by = request.GET.get("sort_by", "newest")
    if sort_by == "oldest":
        news = News.objects.all().order_by("created_at")
    else:
        news = News.objects.all().order_by("-created_at")
    
    paginator = Paginator(news, 3) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, "home.html", {"page_obj": page_obj})


def order_list(request):
    
    status = request.GET.get("status")  
    sort_by = request.GET.get("sort")  

    
    orders = Order.objects.all()

  
    if status:
        orders = orders.filter(status=status)

    
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


def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if order.status == "active":
        order.status = "canceled"
        order.save()
    return redirect("order_list")


def restore_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if order.status == "canceled":
        order.status = "active"
        order.save()
    return redirect("order_list")


def news_list(request):
    sort_by = request.GET.get("sort_by", "newest")
    if sort_by == "oldest":
        news = News.objects.all().order_by("created_at")
    else:  
        news = News.objects.all().order_by("-created_at")

    paginator = Paginator(news, 3)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "news_list.html", {"page_obj": page_obj})


def news_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    related_news = news.get_related_news() 
    return render(request, 'news_details.html', {'news': news, 'related_news': related_news})


@login_required
def add_comment(request, news_id):
    news = get_object_or_404(News, id=news_id)
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        if comment_text:
            Comment.objects.create(
                news=news,
                user=request.user,
                text=comment_text
            )
    return redirect('news_detail', news_id=news_id)


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    news_id = comment.news.id
    if request.user == comment.user or request.user.is_staff:
        comment.delete()
        return redirect('news_detail', news_id=news_id)
    else:
        return HttpResponseForbidden("У вас нет прав на удаление этого комментария.")
