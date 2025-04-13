import os
import sys
import subprocess
import re
import codecs

def run_server():
    # Запускаем сервер и перехватываем вывод
    process = subprocess.Popen(
        ['python', 'manage.py', 'runserver', '127.0.0.1:3000'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
        encoding='utf-8'
    )
    
    # Фильтруем вывод
    for line in process.stdout:
        if not re.search(r'WARNING: This is a development server', line):
            print(line, end='')
    
    process.wait()

if __name__ == "__main__":
    run_server() 