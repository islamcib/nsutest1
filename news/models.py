from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field
from translator.translator import TranslationMixin

class NewsCategory(TranslationMixin, models.Model):
    name = models.CharField(_('Название категории'), max_length=100)
    name_en = models.CharField(_('Название категории (англ.)'), max_length=100, blank=True)
    name_ky = models.CharField(_('Название категории (кырг.)'), max_length=100, blank=True)
    slug = models.SlugField(_('URL'), unique=True)

    class Meta:
        verbose_name = _('Категория новостей')
        verbose_name_plural = _('Категории новостей')

    def __str__(self):
        return self.name

class News(TranslationMixin, models.Model):
    title = models.CharField(_('Заголовок'), max_length=255)
    title_en = models.CharField(_('Заголовок (англ.)'), max_length=255, blank=True)
    title_ky = models.CharField(_('Заголовок (кырг.)'), max_length=255, blank=True)
    slug = models.SlugField(_('URL'), unique=True)
    
    short_description = models.TextField(_('Краткое описание'))
    short_description_en = models.TextField(_('Краткое описание (англ.)'), blank=True)
    short_description_ky = models.TextField(_('Краткое описание (кырг.)'), blank=True)
    
    content = CKEditor5Field(_('Содержание'))
    content_en = CKEditor5Field(_('Содержание (англ.)'), blank=True)
    content_ky = CKEditor5Field(_('Содержание (кырг.)'), blank=True)
    
    image = models.ImageField(_('Изображение'), upload_to='news/')
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, related_name='news')
    author = models.CharField(_('Автор'), max_length=100)
    created_at = models.DateTimeField(_('Дата создания'), default=timezone.now)
    updated_at = models.DateTimeField(_('Дата обновления'), auto_now=True)
    is_published = models.BooleanField(_('Опубликовано'), default=True)

    class Meta:
        verbose_name = _('Новость')
        verbose_name_plural = _('Новости')
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(_('Изображение'), upload_to='news/gallery/')
    description = models.CharField(_('Описание'), max_length=255, blank=True)

    class Meta:
        verbose_name = _('Изображение новости')
        verbose_name_plural = _('Изображения новостей')

    def __str__(self):
        return f"Изображение для {self.news.title}" 