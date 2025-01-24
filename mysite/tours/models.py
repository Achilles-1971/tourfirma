from django.db import models
from django.contrib.auth.models import User  
from django.db.models import Q
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
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)  
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=[
            ('active', 'Активный'),
            ('completed', 'Завершенный'),
            ('canceled', 'Отмененный'),
        ],
        default='active',
    )

class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True) 
    interesting_fact = models.TextField(blank=True, null=True)  
    important_fact = models.TextField(blank=True, null=True)  
    source = models.CharField(max_length=255, blank=True, null=True)  
    def __str__(self):
        return self.title

    def get_related_news(self, limit=5):
        words = self.title.split()
        query = models.Q()
        for word in words:
            query |= models.Q(title__icontains=word)
        return News.objects.filter(query).exclude(id=self.id).order_by('-created_at')[:limit]

class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to="news_gallery/")
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Фото для {self.news.title}"
    
class KeyPoint(models.Model):
    day = models.ForeignKey(
        TourDay,
        on_delete=models.CASCADE,
        related_name='key_points'
    )
    text = models.CharField(max_length=255, verbose_name="Текст ключевого момента")

    ICON_CHOICES = [
        ('bi-geo-alt-fill', 'Геолокация'),
        ('bi-calendar-check-fill', 'Календарь'),
        ('bi-star-fill', 'Звезда'),
        ('bi-check-circle-fill', 'Галочка'),
    ]
    icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='bi-star-fill',
        verbose_name="Иконка (Bootstrap Icons)"
    )

    def __str__(self):
        return f"{self.text[:50]}..."

class Comment(models.Model):
    news = models.ForeignKey(News, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Комментарий от {self.user.username} к {self.news.title}'