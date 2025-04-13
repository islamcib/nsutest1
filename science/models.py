from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field

class ResearchArea(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = CKEditor5Field(verbose_name='Описание')
    image = models.ImageField(upload_to='research_areas/', verbose_name='Изображение')
    slug = models.SlugField(unique=True, verbose_name='URL')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Научное направление'
        verbose_name_plural = 'Научные направления'

class ResearchProject(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = CKEditor5Field(verbose_name='Описание')
    area = models.ForeignKey(ResearchArea, on_delete=models.CASCADE, related_name='projects', verbose_name='Направление')
    leader = models.CharField(max_length=255, verbose_name='Руководитель')
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания')
    slug = models.SlugField(unique=True, verbose_name='URL')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Научный проект'
        verbose_name_plural = 'Научные проекты'

class Publication(models.Model):
    TYPE_CHOICES = [
        ('article', 'Статья'),
        ('book', 'Книга'),
        ('conference', 'Конференция'),
        ('patent', 'Патент'),
    ]
    
    title = models.CharField(max_length=255, verbose_name='Название')
    authors = models.TextField(verbose_name='Авторы')
    year = models.IntegerField(verbose_name='Год')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name='Тип')
    journal = models.CharField(max_length=255, verbose_name='Журнал/Издательство')
    volume = models.CharField(max_length=50, null=True, blank=True, verbose_name='Том')
    issue = models.CharField(max_length=50, null=True, blank=True, verbose_name='Номер')
    pages = models.CharField(max_length=50, null=True, blank=True, verbose_name='Страницы')
    doi = models.CharField(max_length=100, null=True, blank=True, verbose_name='DOI')
    abstract = models.TextField(verbose_name='Аннотация')
    keywords = models.TextField(verbose_name='Ключевые слова')
    file = models.FileField(upload_to='publications/', null=True, blank=True, verbose_name='Файл')
    slug = models.SlugField(unique=True, verbose_name='URL')
    area = models.ForeignKey(ResearchArea, on_delete=models.SET_NULL, null=True, blank=True, related_name='publications', verbose_name='Научное направление')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

class Conference(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания')
    location = models.CharField(max_length=255, verbose_name='Место проведения')
    organizer = models.CharField(max_length=255, verbose_name='Организатор')
    website = models.URLField(null=True, blank=True, verbose_name='Сайт')
    registration_deadline = models.DateField(null=True, blank=True, verbose_name='Срок регистрации')
    is_active = models.BooleanField(default=True, verbose_name='Активна')
    slug = models.SlugField(unique=True, verbose_name='URL')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Конференция'
        verbose_name_plural = 'Конференции' 