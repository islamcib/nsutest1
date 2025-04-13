from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import ResearchArea, ResearchProject, Publication, Conference

def science(request):
    areas = ResearchArea.objects.all()[:3]
    projects = ResearchProject.objects.all()[:3]
    publications = Publication.objects.all().order_by('-year')[:3]
    conferences = Conference.objects.all()[:3]
    return render(request, 'science/science.html', {
        'areas': areas,
        'projects': projects,
        'publications': publications,
        'conferences': conferences
    })

def research_areas(request):
    areas = ResearchArea.objects.all()
    return render(request, 'science/research_areas.html', {'areas': areas})

def research_area_detail(request, slug):
    area = get_object_or_404(ResearchArea, slug=slug)
    projects = area.projects.all()
    publications = Publication.objects.filter(area=area)
    conferences = Conference.objects.filter(is_active=True)
    return render(request, 'science/research_area_detail.html', {
        'area': area,
        'projects': projects,
        'publications': publications,
        'conferences': conferences
    })

def research_project_detail(request, slug):
    project = get_object_or_404(ResearchProject, slug=slug)
    return render(request, 'science/research_project_detail.html', {'project': project})

def publications(request):
    publications_list = Publication.objects.all().order_by('-year')
    
    # Фильтрация по типу
    pub_type = request.GET.get('type')
    if pub_type:
        publications_list = publications_list.filter(type=pub_type)
    
    # Поиск
    search_query = request.GET.get('search')
    if search_query:
        publications_list = publications_list.filter(title__icontains=search_query)
    
    # Пагинация
    paginator = Paginator(publications_list, 10)
    page = request.GET.get('page')
    publications = paginator.get_page(page)
    
    return render(request, 'science/publications.html', {
        'publications': publications,
        'is_paginated': True,
        'page_obj': publications
    })

def publication_detail(request, slug):
    publication = get_object_or_404(Publication, slug=slug)
    related_publications = Publication.objects.filter(
        type=publication.type
    ).exclude(id=publication.id)[:5]
    return render(request, 'science/publication_detail.html', {
        'publication': publication,
        'related_publications': related_publications
    })

def conferences(request):
    conferences_list = Conference.objects.all().order_by('-start_date')
    
    # Фильтрация по статусу
    status = request.GET.get('status')
    if status == 'active':
        conferences_list = conferences_list.filter(is_active=True)
    elif status == 'past':
        conferences_list = conferences_list.filter(is_active=False)
    
    # Поиск
    search_query = request.GET.get('search')
    if search_query:
        conferences_list = conferences_list.filter(title__icontains=search_query)
    
    # Пагинация
    paginator = Paginator(conferences_list, 10)
    page = request.GET.get('page')
    conferences = paginator.get_page(page)
    
    return render(request, 'science/conferences.html', {
        'conferences': conferences,
        'is_paginated': True,
        'page_obj': conferences
    })

def conference_detail(request, slug):
    conference = get_object_or_404(Conference, slug=slug)
    return render(request, 'science/conference_detail.html', {'conference': conference}) 