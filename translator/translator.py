from googletrans import Translator
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from deep_translator import GoogleTranslator
from django.db import models

class AutoTranslator:
    def __init__(self):
        self.translator = Translator()
        self.supported_languages = ['ru', 'en', 'ky']  # Добавьте нужные языки

    def translate_text(self, text, target_lang):
        try:
            if not text or not isinstance(text, str):
                return text
            
            # Проверяем, является ли текст уже переведенным
            if target_lang == settings.LANGUAGE_CODE:
                return text
                
            translation = self.translator.translate(text, dest=target_lang)
            return translation.text
        except Exception as e:
            print(f"Ошибка перевода: {str(e)}")
            return text

    def translate_model(self, model_instance, fields_to_translate):
        """
        Автоматически переводит указанные поля модели
        """
        for field in fields_to_translate:
            if hasattr(model_instance, field):
                original_text = getattr(model_instance, field)
                if original_text:
                    for lang in self.supported_languages:
                        if lang != settings.LANGUAGE_CODE:
                            translated_field = f"{field}_{lang}"
                            if hasattr(model_instance, translated_field):
                                translated_text = self.translate_text(original_text, lang)
                                setattr(model_instance, translated_field, translated_text)
        
        return model_instance

class TranslationMixin:
    def translate_field(self, field_name, target_lang):
        """
        Автоматически переводит указанное поле на целевой язык
        """
        original_text = getattr(self, field_name)
        if not original_text:
            return ""
            
        try:
            translator = GoogleTranslator(source='auto', target=target_lang)
            translated_text = translator.translate(original_text)
            return translated_text
        except Exception as e:
            print(f"Ошибка перевода: {str(e)}")
            return original_text

    def save(self, *args, **kwargs):
        """
        Автоматически переводит поля при сохранении модели
        """
        if not self.pk:  # Только для новых объектов
            for field in self._meta.fields:
                if isinstance(field, models.CharField) or isinstance(field, models.TextField):
                    field_name = field.name
                    if not field_name.endswith(('_en', '_ky')):
                        # Переводим на английский
                        en_field = f"{field_name}_en"
                        if hasattr(self, en_field):
                            setattr(self, en_field, self.translate_field(field_name, 'en'))
                        # Переводим на кыргызский
                        ky_field = f"{field_name}_ky"
                        if hasattr(self, ky_field):
                            setattr(self, ky_field, self.translate_field(field_name, 'ky'))
        
        super().save(*args, **kwargs)

# Создаем экземпляр переводчика
translator = AutoTranslator() 