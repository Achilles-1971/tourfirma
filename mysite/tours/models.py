from django.db import models
from django.contrib.auth.models import User  

class Tour(models.Model):
    name = models.CharField(max_length=255) 
    description = models.TextField(blank=True)  
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  
    start_date = models.DateField(null=True, blank=True) 
    end_date = models.DateField(null=True, blank=True)  
    is_active = models.BooleanField(default=True)  
    def __str__(self):
        return self.name


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