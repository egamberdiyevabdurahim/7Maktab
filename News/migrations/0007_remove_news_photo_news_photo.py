# Generated by Django 5.0.1 on 2024-01-29 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0006_news_viewed_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='photo',
        ),
        migrations.AddField(
            model_name='news',
            name='photo',
            field=models.ImageField(null=True, upload_to='news_photos/'),
        ),
    ]
