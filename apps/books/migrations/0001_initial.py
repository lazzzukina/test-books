# Generated by Django 5.0.4 on 2024-08-16 18:10

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('published_date', models.DateField(blank=True, null=True)),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('cover', models.URLField(blank=True, null=True)),
                ('language', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
                'db_table': 'books',
            },
        ),
    ]
