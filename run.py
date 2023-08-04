# Для запуска проекта на сервере командой python run.py

import subprocess
import threading


def run_django():
    subprocess.call(['python', 'manage.py', 'runserver'])


def run_tg_bot():
    subprocess.call(['python', 'bot.py'])


if __name__ == '__main__':
    django_thread = threading.Thread(target=run_django)
    telegram_thread = threading.Thread(target=run_tg_bot)

    django_thread.start()
    telegram_thread.start()

    django_thread.join()
    telegram_thread.join()
