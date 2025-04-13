from django.db import models
from django.utils.translation import gettext_lazy as _

class UniversityInfo(models.Model):
    title = models.CharField(_('Название'), max_length=255)
    mission = models.TextField(_('Миссия университета'))
    hymn = models.TextField(_('Гимн университета'))
    address = models.TextField(_('Адрес'))
    phone = models.CharField(_('Телефон'), max_length=20)
    email = models.EmailField(_('Email'))
    logo = models.ImageField(_('Логотип'), upload_to='university/')
    banner = models.ImageField(_('Баннер'), upload_to='university/')

    class Meta:
        verbose_name = _('Информация об университете')
        verbose_name_plural = _('Информация об университете')

    def __str__(self):
        return self.title

class Building(models.Model):
    name = models.CharField(_('Название корпуса'), max_length=255)
    description = models.TextField(_('Описание'))
    image = models.ImageField(_('Изображение'), upload_to='buildings/')
    address = models.TextField(_('Адрес корпуса'))

    class Meta:
        verbose_name = _('Корпус')
        verbose_name_plural = _('Корпуса')

    def __str__(self):
        return self.name 