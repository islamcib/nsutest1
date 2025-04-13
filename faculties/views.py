from django.shortcuts import render, get_object_or_404
from .models import Faculty, Department, Specialization

def faculty_list(request):
    faculties = Faculty.objects.all()
    context = {
        'faculties': faculties,
    }
    return render(request, 'faculties/list.html', context)

def faculty_detail(request, slug):
    faculty = get_object_or_404(Faculty, slug=slug)
    departments = faculty.departments.all()
    specializations = faculty.specializations.all()

    context = {
        'faculty': faculty,
        'departments': departments,
        'specializations': specializations,
    }
    return render(request, 'faculties/detail.html', context)

def department_detail(request, faculty_slug, department_slug):
    faculty = get_object_or_404(Faculty, slug=faculty_slug)
    department = get_object_or_404(Department, faculty=faculty, slug=department_slug)

    context = {
        'faculty': faculty,
        'department': department,
    }
    return render(request, 'faculties/department_detail.html', context)

def specialization_detail(request, faculty_slug, specialization_slug):
    faculty = get_object_or_404(Faculty, slug=faculty_slug)
    specialization = get_object_or_404(Specialization, faculty=faculty, slug=specialization_slug)

    context = {
        'faculty': faculty,
        'specialization': specialization,
    }
    return render(request, 'faculties/specialization_detail.html', context) 