# Generated by Django 4.2 on 2025-01-19 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0004_order_is_active_order_order_date_alter_order_tour_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_active',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('active', 'Активный'), ('completed', 'Завершенный'), ('canceled', 'Отмененный')], default='active', max_length=10),
        ),
    ]
