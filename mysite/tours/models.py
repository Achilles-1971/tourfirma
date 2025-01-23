from django.db import models
from django.contrib.auth.models import User  

from django.db import models

class Tour(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to='tour_images/', blank=True, null=True)
    gif = models.ImageField(upload_to='tours_gifs/', blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)  
    longitude = models.FloatField(blank=True, null=True) 

    def __str__(self):
        return self.name


class TourDay(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='days')
    day_number = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='tour_day_images/', blank=True, null=True)

    def __str__(self):
        return f"День {self.day_number} - {self.title}"
    def __str__(self):
        return f"{self.tour.name} - День {self.day_number}"


class Order(models.Model):
    STATUS_CHOICES = [
        ('active', 'Активный'),
        ('completed', 'Завершенный'),
        ('canceled', 'Отмененный'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f"{self.user} - {self.tour} ({self.status})"

class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to="news_images/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title