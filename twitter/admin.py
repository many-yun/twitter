from django.contrib import admin
from .models import Twit

class TwitAdmin(admin.ModelAdmin):
    search_fields = ['content']

admin.site.register(Twit, TwitAdmin)