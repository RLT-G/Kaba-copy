import os
from a_setting.settings.base import *


DEBUG = True
ALLOWED_HOSTS = []


# отправка сессий только через https
CSRF_COOKIE_SECURE = False


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'db_kaba',
    #     'HOST': '127.0.0.1',
    #     # 'HOST': 'localhost',
    #     'PORT': '3306',
    #     'USER': 'root',
    #     'PASSWORD': '',
    # }
}


# для фото
MEDIA_URL = '/media/'