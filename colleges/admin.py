from django.contrib import admin
from .models import College

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'director', 'established_date', 'created_at')
    list_filter = ('established_date', 'created_at')
    search_fields = ('name', 'director', 'description')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'updated_at')
