from django.urls import path
from . import views

app_name = 'education'

urlpatterns = [
    path('', views.program_list, name='program_list'),
    path('programs/<slug:slug>/', views.program_detail, name='program_detail'),
    path('courses/<slug:slug>/', views.course_detail, name='course_detail'),
] 