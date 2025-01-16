from django.db import models
from django.contrib.auth.models import User  # Используем встроенную модель пользователя

class Tour(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)  # Может ли тур быть заказан?

    def __str__(self):
        return self.name

class Order(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)  # Активен ли заказ?

    def __str__(self):
        return f"Заказ {self.id} - {self.tour.name}"