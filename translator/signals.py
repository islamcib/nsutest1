from django.db.models.signals import post_save
from django.dispatch import receiver
from .translator import translator

def register_translation(model_class, fields_to_translate):
    """
    Регистрирует сигнал для автоматического перевода указанной модели
    """
    @receiver(post_save, sender=model_class)
    def translate_model(sender, instance, created, **kwargs):
        if created or kwargs.get('update_fields'):
            translator.translate_model(instance, fields_to_translate)
            instance.save(update_fields=[f"{field}_{lang}" 
                                       for field in fields_to_translate 
                                       for lang in translator.supported_languages 
                                       if lang != translator.supported_languages[0]]) 