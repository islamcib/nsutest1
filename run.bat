@echo off
chcp 65001 > nul
python manage.py runserver 127.0.0.1:3000 | findstr /V "WARNING: This is a development server" 