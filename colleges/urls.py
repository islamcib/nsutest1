from django.urls import path
from . import views

app_name = 'colleges'

urlpatterns = [
    path('', views.college_list, name='college_list'),
    path('<slug:slug>/', views.college_detail, name='college_detail'),
] 