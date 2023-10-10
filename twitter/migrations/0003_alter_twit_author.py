# Generated by Django 4.0.3 on 2023-10-10 00:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('twitter', '0002_alter_twit_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twit',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='own_twit', to=settings.AUTH_USER_MODEL),
        ),
    ]
