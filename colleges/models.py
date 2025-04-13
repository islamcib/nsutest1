from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field

class College(models.Model):
    name = models.CharField(_('Название'), max_length=255)
    slug = models.SlugField(_('URL'), max_length=255, unique=True, blank=True)
    description = CKEditor5Field(_('Описание'))
    image = models.ImageField(_('Изображение'), upload_to='colleges/')
    address = models.CharField(_('Адрес'), max_length=255)
    phone = models.CharField(_('Телефон'), max_length=20)
    email = models.EmailField(_('Email'))
    director = models.CharField(_('Директор'), max_length=255)
    established_date = models.DateField(_('Дата основания'))
    website = models.URLField(_('Веб-сайт'), blank=True)
    facebook = models.URLField(_('Facebook'), blank=True)
    instagram = models.URLField(_('Instagram'), blank=True)
    telegram = models.URLField(_('Telegram'), blank=True)
    created_at = models.DateTimeField(_('Создано'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Обновлено'), auto_now=True)

    class Meta:
        verbose_name = _('Колледж')
        verbose_name_plural = _('Колледжи')
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
