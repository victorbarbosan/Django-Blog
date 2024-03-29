# Generated by Django 4.0.3 on 2022-04-18 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),                
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('image', models.ImageField(upload_to=None)),
                ('excerpt', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, default='')),
                ('content', models.TextField()),
            ],
        ),
    ]
