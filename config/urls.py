from django.contrib import admin
from django.urls import path, include
from twitter import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('twitter/', include('twitter.urls')),
    path('common/', include('common.urls')), 
    path('', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
