# Generated by Django 4.0.3 on 2023-09-25 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_user_pp_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pp',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
