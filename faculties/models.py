from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field

class Faculty(models.Model):
    name = models.CharField(_('Название факультета'), max_length=255)
    description = CKEditor5Field(_('Описание'))
    image = models.ImageField(_('Изображение'), upload_to='faculties/')
    dean = models.CharField(_('Декан'), max_length=255)
    email = models.EmailField(_('Email'))
    phone = models.CharField(_('Телефон'), max_length=20)
    address = models.TextField(_('Адрес'))
    slug = models.SlugField(_('URL'), max_length=255, unique=True, blank=True)

    class Meta:
        verbose_name = _('Факультет')
        verbose_name_plural = _('Факультеты')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Department(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='departments')
    name = models.CharField(_('Название кафедры'), max_length=255)
    description = CKEditor5Field(_('Описание'))
    head = models.CharField(_('Заведующий кафедрой'), max_length=255)
    email = models.EmailField(_('Email'))
    phone = models.CharField(_('Телефон'), max_length=20)

    class Meta:
        verbose_name = _('Кафедра')
        verbose_name_plural = _('Кафедры')

    def __str__(self):
        return f"{self.name} ({self.faculty.name})"

class Specialization(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='specializations')
    name = models.CharField(_('Название специальности'), max_length=255)
    code = models.CharField(_('Код специальности'), max_length=20)
    description = models.TextField(_('Описание'))
    duration = models.IntegerField(_('Срок обучения (лет)'))
    degree = models.CharField(_('Степень'), max_length=100)

    class Meta:
        verbose_name = _('Специальность')
        verbose_name_plural = _('Специальности')

    def __str__(self):
        return f"{self.name} ({self.faculty.name})" 