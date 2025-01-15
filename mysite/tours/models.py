from django.db import models
from django.contrib.auth.models import User  # Используем встроенную модель пользователя

class Tour(models.Model):
    name = models.CharField(max_length=200)  # Название тура
    description = models.TextField()  # Описание тура
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена тура
    start_date = models.DateField()  # Дата начала тура
    end_date = models.DateField()  # Дата окончания тура

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)  # Связь с туром
    order_date = models.DateField(auto_now_add=True)  # Дата заказа (автоматически добавляется при создании)

    def __str__(self):
        return f"Order by {self.user.username} for {self.tour.name}"

