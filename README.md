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

Официальный веб-сайт Нарынского государственного университета, разработанный с использованием Django.

## Описание проекта

Этот проект представляет собой многоязычный веб-сайт университета с поддержкой трех языков:
- Русский
- Английский
- Кыргызский

## Основные функции

- Многоязычный интерфейс
- Система автоматического перевода контента
- Административная панель для управления контентом
- Интеграция с социальными сетями
- Адаптивный дизайн

## Технологии

- Python 3.8+
- Django 4.2+
- PostgreSQL
- HTML5/CSS3
- JavaScript
- Bootstrap 5

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/islamcib/nsu-website.git
cd nsu-website
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Создайте файл .env в корневой директории и настройте переменные окружения:
```bash
DEBUG=True
SECRET_KEY=ваш_секретный_ключ
DATABASE_URL=postgres://user:password@localhost:5432/nsu_db
```

5. Примените миграции:
```bash
python manage.py migrate
```

6. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```

7. Запустите сервер разработки:
```bash
python manage.py runserver
```

## Структура проекта

```
nsu_website/
├── nsu_website/          # Основное приложение Django
├── translator/           # Приложение для автоматического перевода
├── static/              # Статические файлы (CSS, JS, изображения)
├── templates/           # HTML шаблоны
├── media/               # Загружаемые пользователем файлы
└── requirements.txt     # Зависимости проекта
```

## Лицензия

Этот проект распространяется под лицензией MIT.

## Контакты

По всем вопросам обращайтесь:
- Email: info@nsu.kg
- Телефон: +996 (0) 555 123 456

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