# Инструкция по развертыванию сайта на сервере Кыргыз Телеком

## 1. Подготовка локальной версии

1. Соберите все статические файлы:
```bash
python manage.py collectstatic
```

2. Создайте резервную копию базы данных:
```bash
python manage.py dumpdata > backup.json
```

3. Подготовьте файл .env с настройками:
```
DEBUG=False
SECRET_KEY=ваш-секретный-ключ
ALLOWED_HOSTS=ваш-домен.kg
DATABASE_URL=postgres://user:password@localhost:5432/dbname
```

## 2. Подготовка сервера

1. Установите необходимые пакеты:
```bash
sudo apt update
sudo apt install python3-pip python3-venv nginx postgresql
```

2. Создайте пользователя для приложения:
```bash
sudo useradd -m -s /bin/bash nsu
sudo passwd nsu
```

3. Настройте PostgreSQL:
```bash
sudo -u postgres psql
CREATE DATABASE nsu_db;
CREATE USER nsu_user WITH PASSWORD 'ваш-пароль';
GRANT ALL PRIVILEGES ON DATABASE nsu_db TO nsu_user;
```

## 3. Развертывание приложения

1. Скопируйте файлы на сервер:
```bash
scp -r /путь/к/проекту nsu@ваш-сервер:/home/nsu/
```

2. На сервере:
```bash
cd /home/nsu
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Настройте Nginx:
```nginx
server {
    listen 80;
    server_name ваш-домен.kg;

    location /static/ {
        alias /home/nsu/staticfiles/;
    }

    location /media/ {
        alias /home/nsu/media/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

4. Настройте Gunicorn:
```bash
sudo nano /etc/systemd/system/nsu.service
```

```ini
[Unit]
Description=NSU Gunicorn Service
After=network.target

[Service]
User=nsu
Group=www-data
WorkingDirectory=/home/nsu
Environment="PATH=/home/nsu/venv/bin"
ExecStart=/home/nsu/venv/bin/gunicorn --workers 3 --bind 127.0.0.1:8000 nsu.wsgi:application

[Install]
WantedBy=multi-user.target
```

5. Запустите сервисы:
```bash
sudo systemctl start nsu
sudo systemctl enable nsu
sudo systemctl restart nginx
```

## 4. Настройка SSL (HTTPS)

1. Установите certbot:
```bash
sudo apt install certbot python3-certbot-nginx
```

2. Получите сертификат:
```bash
sudo certbot --nginx -d ваш-домен.kg
```

## 5. Мониторинг и обслуживание

1. Проверка статуса:
```bash
sudo systemctl status nsu
sudo systemctl status nginx
```

2. Логи:
```bash
sudo journalctl -u nsu
sudo tail -f /var/log/nginx/error.log
```

3. Автоматические бэкапы:
```bash
# Добавьте в crontab:
0 3 * * * /home/nsu/venv/bin/python /home/nsu/manage.py dumpdata > /home/nsu/backups/backup_$(date +\%Y\%m\%d).json
```

## 6. Обновление сайта

1. Остановите сервис:
```bash
sudo systemctl stop nsu
```

2. Обновите код:
```bash
cd /home/nsu
git pull  # или scp новые файлы
```

3. Обновите зависимости:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

4. Примените миграции:
```bash
python manage.py migrate
```

5. Соберите статические файлы:
```bash
python manage.py collectstatic --noinput
```

6. Запустите сервис:
```bash
sudo systemctl start nsu
```

## 7. Контакты поддержки

- Техническая поддержка Кыргыз Телеком: +996 (312) 65-00-00
- Администратор сайта: ваш-email@nsu.kg
- Телефон администратора: ваш-телефон 