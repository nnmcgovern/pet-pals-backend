# Generated by Django 4.2.4 on 2023-08-30 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0005_alter_comment_post_alter_like_post'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField()),
                ('first_name', models.CharField()),
                ('last_name', models.CharField()),
                ('email', models.CharField()),
                ('password', models.CharField()),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.comment')),
                ('like', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='posts.like')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]