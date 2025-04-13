from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.news_list, name='list'),
    path('<slug:slug>/', views.news_detail, name='detail'),
    path('category/<slug:category_slug>/', views.news_by_category, name='category'),
] 