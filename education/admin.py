from django.contrib import admin
from .models import Program, Course

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'degree', 'duration')
    list_filter = ('degree',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'program', 'credits')
    list_filter = ('program',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)} 