# Автоматический переводчик

Этот проект представляет собой Django-приложение для автоматического перевода текста на различные языки (русский, английский, кыргызский).

## Функциональность

- Автоматический перевод полей моделей Django
- Поддержка множества языков
- Простая интеграция с Django моделями
- Использование Google Translate API

## Установка

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Добавьте `translator` в `INSTALLED_APPS` вашего Django проекта.

## Использование

```python
from translator.translator import TranslationMixin

class YourModel(TranslationMixin, models.Model):
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    title_ky = models.CharField(max_length=200)
```

# Сайт Нарынского государственного университета

## Описание
Официальный сайт Нарынского государственного университета, созданный с использованием Django, Bootstrap и других современных технологий.

## Функциональность
- Главная страница с баннером и основной информацией
- Факультеты и колледжи с отдельными админ-панелями
- Новости
- Образование
- Наука
- Контакты
- Абитуриентам

## Установка
1. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  
venv\Scripts\activate    
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Примените миграции:
```bash
python manage.py migrate
```

4. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```

5. Запустите сервер:
```bash
python manage.py runserver
```

# Инструкция по запуску сайта

## Подготовка к запуску

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Подготовьте базу данных:
```bash
python manage.py migrate
```

3. Соберите статические файлы:
```bash
python manage.py collectstatic
```

4. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```

## Запуск сайта

1. Для разработки:
```bash
python manage.py runserver 127.0.0.1:8000
```

2. Для продакшена:
```bash
python manage.py runserver 0.0.0.0:8000
```

## Важные замечания

1. Убедитесь, что все необходимые директории созданы:
   - staticfiles/
   - media/
   - logs/
   - cache/

2. Проверьте права доступа к директориям:
   - staticfiles/ - чтение
   - media/ - чтение/запись
   - logs/ - чтение/запись
   - cache/ - чтение/запись

3. Для продакшена рекомендуется использовать:
   - Nginx как веб-сервер
   - Gunicorn как WSGI-сервер
   - PostgreSQL как базу данных
   - Redis для кэширования

## Безопасность

1. Измените SECRET_KEY в settings.py
2. Настройте ALLOWED_HOSTS
3. Включите SSL
4. Настройте бэкапы базы данных
5. Регулярно обновляйте зависимости 