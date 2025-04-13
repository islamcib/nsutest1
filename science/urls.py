from django.urls import path
from . import views

app_name = 'science'

urlpatterns = [
    path('', views.science, name='science'),
    path('research/', views.research_areas, name='research_areas'),
    path('research/<slug:slug>/', views.research_area_detail, name='research_area_detail'),
    path('projects/<slug:slug>/', views.research_project_detail, name='research_project_detail'),
    path('publications/', views.publications, name='publications'),
    path('publications/<slug:slug>/', views.publication_detail, name='publication_detail'),
    path('conferences/', views.conferences, name='conferences'),
    path('conferences/<slug:slug>/', views.conference_detail, name='conference_detail'),
] 