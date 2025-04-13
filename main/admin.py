from django.contrib import admin
from .models import UniversityInfo, Building

@admin.register(UniversityInfo)
class UniversityInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'phone')
    search_fields = ('title', 'email', 'phone')

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address') 