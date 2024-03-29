# Generated by Django 5.0.1 on 2024-01-28 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0004_alter_news_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Haqida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='news_photo/')),
            ],
        ),
        migrations.RemoveField(
            model_name='news',
            name='photo',
        ),
        migrations.AddField(
            model_name='news',
            name='photo',
            field=models.ManyToManyField(to='News.photo'),
        ),
    ]
