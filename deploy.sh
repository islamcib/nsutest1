#!/bin/bash

# Настройки
SERVER="ваш-сервер.kg"
USER="nsu"
DOMAIN="ваш-домен.kg"
DB_NAME="nsu_db"
DB_USER="nsu_user"
DB_PASS="ваш-пароль"

# Сборка статических файлов
echo "Сборка статических файлов..."
python manage.py collectstatic --noinput

# Создание резервной копии
echo "Создание резервной копии..."
python manage.py dumpdata > backup_$(date +%Y%m%d).json

# Копирование файлов на сервер
echo "Копирование файлов на сервер..."
rsync -avz --exclude 'venv' --exclude '.git' --exclude '__pycache__' ./ $USER@$SERVER:/home/$USER/

# Подключение к серверу и выполнение команд
echo "Настройка сервера..."
ssh $USER@$SERVER << EOF
    cd /home/$USER
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    
    # Настройка базы данных
    sudo -u postgres psql -c "CREATE DATABASE $DB_NAME;"
    sudo -u postgres psql -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASS';"
    sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;"
    
    # Применение миграций
    python manage.py migrate
    
    # Перезапуск сервисов
    sudo systemctl restart nsu
    sudo systemctl restart nginx
EOF

echo "Развертывание завершено!" 