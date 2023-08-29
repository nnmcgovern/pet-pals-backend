# Generated by Django 4.2.4 on 2023-08-29 14:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField()),
                ('user_id', models.IntegerField()),
                ('post_id', models.IntegerField()),
                ('updated_at', models.DateField(default=datetime.date.today)),
                ('created_at', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField()),
                ('post_id', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('image', models.CharField()),
                ('age', models.IntegerField()),
                ('animal_type', models.CharField()),
                ('breed', models.CharField()),
                ('description', models.CharField()),
                ('gender', models.CharField()),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
