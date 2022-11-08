# Generated by Django 3.2.13 on 2022-11-04 02:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_celsius_check'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='celsius_check',
        ),
        migrations.AddField(
            model_name='user',
            name='celsius_minus',
            field=models.ManyToManyField(related_name='minus_celsius', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='celsius_plus',
            field=models.ManyToManyField(related_name='plus_celsius', to=settings.AUTH_USER_MODEL),
        ),
    ]
