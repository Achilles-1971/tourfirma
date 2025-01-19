from django.contrib import admin
from .models import Tour, Order

admin.site.register(Tour)
admin.site.register(Order)
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')


