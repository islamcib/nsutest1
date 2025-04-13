from django.db import models
from django.utils.text import slugify

class Program(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название программы')
    description = models.TextField(verbose_name='Описание')
    duration = models.CharField(max_length=50, verbose_name='Продолжительность')
    degree = models.CharField(max_length=100, verbose_name='Степень')
    slug = models.SlugField(unique=True, verbose_name='URL')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Образовательная программа'
        verbose_name_plural = 'Образовательные программы'

class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание')
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='courses', verbose_name='Программа')
    credits = models.IntegerField(verbose_name='Кредиты')
    slug = models.SlugField(unique=True, verbose_name='URL')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы' 