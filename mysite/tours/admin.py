from django.contrib import admin
from .models import Tour, Order, News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Отображение заголовка и даты создания
    search_fields = ('title', 'description')  # Поля для поиска


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'start_date', 'end_date', 'image_preview')  # Отображаемые столбцы
    list_filter = ('start_date', 'end_date')  # Фильтрация по дате начала и окончания
    search_fields = ('name', 'description')  # Поиск по имени и описанию
    readonly_fields = ('image_preview',)  # Поле предпросмотра только для чтения
    fields = ('name', 'description', 'price', 'start_date', 'end_date', 'latitude', 'longitude', 'image', 'gif', 'image_preview')  # Поля формы в админке

    def image_preview(self, obj):
        """Предпросмотр изображения для тура."""
        if obj.image:
            return f'<img src="{obj.image.url}" style="height: 100px;"/>'
        return "Нет изображения"
    image_preview.allow_tags = True
    image_preview.short_description = "Предпросмотр"  # Заголовок в админке


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'tour', 'order_date', 'status')  # Отображаемые столбцы
    list_filter = ('status', 'order_date')  # Фильтрация по статусу и дате заказа
    search_fields = ('user__username', 'tour__name')  # Поиск по пользователю и названию тура
