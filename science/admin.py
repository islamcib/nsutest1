from django.contrib import admin
from .models import ResearchArea, ResearchProject, Publication, Conference

@admin.register(ResearchArea)
class ResearchAreaAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(ResearchProject)
class ResearchProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'area', 'leader', 'start_date', 'end_date')
    list_filter = ('area', 'start_date', 'end_date')
    search_fields = ('title', 'description', 'leader')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'type', 'journal')
    list_filter = ('type', 'year')
    search_fields = ('title', 'authors', 'journal')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'location', 'is_active')
    list_filter = ('is_active', 'start_date', 'end_date')
    search_fields = ('title', 'description', 'location', 'organizer')
    prepopulated_fields = {'slug': ('title',)} 