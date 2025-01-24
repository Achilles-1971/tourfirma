from django.contrib import admin
from .models import Tour, TourDay, KeyPoint, Order, News, NewsImage


class KeyPointInline(admin.TabularInline):
    model = KeyPoint
    extra = 1
    fields = ('text', 'icon')


class TourDayInline(admin.TabularInline):
    model = TourDay
    extra = 1


class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 3


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
    fields = ('title', 'content', 'image', 'interesting_fact', 'important_fact', 'source', 'created_at')
    readonly_fields = ('created_at',)
    inlines = [NewsImageInline]


@admin.register(TourDay)
class TourDayAdmin(admin.ModelAdmin):
    inlines = [KeyPointInline]


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'start_date', 'end_date', 'image_preview')
    inlines = [TourDayInline]
    list_filter = ('start_date', 'end_date')
    search_fields = ('name', 'description')
    readonly_fields = ('image_preview',)
    fields = (
        'name', 'description', 'price',
        'start_date', 'end_date',
        'latitude', 'longitude',
        'image', 'gif',
        'image_preview'
    )

    def image_preview(self, obj):
        """Предпросмотр изображения для тура в админке."""
        if obj.image:
            return f'<img src="{obj.image.url}" style="height: 100px;"/>'
        return "Нет изображения"
    image_preview.allow_tags = True
    image_preview.short_description = "Предпросмотр"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'tour', 'order_date', 'status')
    list_filter = ('status', 'order_date')
    search_fields = ('user__username', 'tour__name')
