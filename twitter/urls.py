from django.urls import path
from . import views

app_name = 'twitter'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.twit_create, name='twit_create'),
    path('delete/<int:twit_id>', views.twit_delete, name='twit_delete'),
    path('<int:twit_id>/', views.detail, name='detail'),
    path('user/<int:user_id>/', views.mypage, name='mypage'),
]
