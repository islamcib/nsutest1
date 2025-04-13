from django.contrib import admin
from .models import Faculty, Department, Specialization

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'dean', 'email', 'phone')
    search_fields = ('name', 'dean', 'email', 'phone')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty', 'head', 'email', 'phone')
    search_fields = ('name', 'head', 'email', 'phone')
    list_filter = ('faculty',)

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty', 'code', 'duration', 'degree')
    search_fields = ('name', 'code')
    list_filter = ('faculty', 'degree') 