from django.contrib import admin
from django.urls import path, include
from twitter import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('twitter/', include('twitter.urls')),
    path('common/', include('common.urls')), 
    path('', views.index, name='index'),
]
