from django.shortcuts import render, get_object_or_404
from .models import News, NewsCategory

def news_list(request):
    news = News.objects.filter(is_published=True).order_by('-created_at')
    categories = NewsCategory.objects.all()

    context = {
        'news': news,
        'categories': categories,
    }
    return render(request, 'news/list.html', context)

def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug, is_published=True)
    related_news = News.objects.filter(
        category=news.category,
        is_published=True
    ).exclude(id=news.id).order_by('-created_at')[:3]

    context = {
        'news': news,
        'related_news': related_news,
    }
    return render(request, 'news/detail.html', context)

def news_by_category(request, category_slug):
    category = get_object_or_404(NewsCategory, slug=category_slug)
    news = News.objects.filter(category=category, is_published=True).order_by('-created_at')
    categories = NewsCategory.objects.all()

    context = {
        'category': category,
        'news': news,
        'categories': categories,
    }
    return render(request, 'news/category.html', context) 