from django.shortcuts import render, get_object_or_404
from .models import Program, Course

def program_list(request):
    programs = Program.objects.all()
    return render(request, 'education/program_list.html', {'programs': programs})

def program_detail(request, slug):
    program = get_object_or_404(Program, slug=slug)
    courses = program.courses.all()
    return render(request, 'education/program_detail.html', {'program': program, 'courses': courses})

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, 'education/course_detail.html', {'course': course}) 