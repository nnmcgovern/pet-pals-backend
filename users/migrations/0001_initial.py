# Generated by Django 4.2.4 on 2023-08-28 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField()),
                ('first_name', models.CharField()),
                ('last_name', models.CharField()),
                ('email', models.CharField()),
                ('password', models.CharField()),
            ],
        ),
    ]