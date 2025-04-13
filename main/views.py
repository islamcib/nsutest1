from django.shortcuts import render
from django.core.cache import cache
from .models import UniversityInfo, Building
from faculties.models import Faculty
from news.models import News
from colleges.models import College

def get_cached_data():
    # Кэшируем данные на 1 час
    cache_key = 'home_page_data'
    data = cache.get(cache_key)
    
    if data is None:
        data = {
            'university_info': UniversityInfo.objects.first(),
            'buildings': Building.objects.all(),
            'faculties': Faculty.objects.all(),
            'colleges': College.objects.all(),
            'latest_news': News.objects.select_related('category').all()[:3]
        }
        cache.set(cache_key, data, 3600)  # 1 час кэширования
    
    return data

def home(request):
    data = get_cached_data()
    return render(request, 'main/home.html', data)

def about(request):
    data = get_cached_data()
    return render(request, 'main/about.html', data) 