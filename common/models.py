from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField('phone', blank=True, max_length=20)
    pp = models.ImageField(upload_to='', null=True, blank=True)
    title = models.CharField('title', max_length=64, blank=True)
    class Meta:
        db_table = 'user'