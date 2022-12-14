# Generated by Django 3.2.13 on 2022-11-04 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_article_unlike_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Popularsearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terms', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('searchCount', models.IntegerField(default=1)),
            ],
        ),
    ]
