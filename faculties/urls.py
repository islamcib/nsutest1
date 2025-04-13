from django.urls import path
from . import views

app_name = 'faculties'

urlpatterns = [
    path('', views.faculty_list, name='list'),
    path('<slug:slug>/', views.faculty_detail, name='detail'),
    path('<slug:faculty_slug>/departments/<slug:department_slug>/', views.department_detail, name='department_detail'),
    path('<slug:faculty_slug>/specializations/<slug:specialization_slug>/', views.specialization_detail, name='specialization_detail'),
] 