from django.shortcuts import render, get_object_or_404
from .models import College

# Create your views here.

def college_list(request):
    colleges = College.objects.all()
    return render(request, 'colleges/college_list.html', {
        'colleges': colleges,
    })

def college_detail(request, slug):
    college = get_object_or_404(College, slug=slug)
    return render(request, 'colleges/college_detail.html', {
        'college': college,
    })
