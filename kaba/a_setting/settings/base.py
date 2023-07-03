import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6nw*xv!(2jvso%4a^9hnf(26p2o+9l)azxil+89122c!6w*q&8'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Рекламный сервис
    'ad.apps.AdConfig',
    # Сервис для регистрации и авторизации
    'c_users.apps.CUsersConfig',
    # Доп сервис, что требуют большинство django дополнений
    'django.contrib.sites',
    # allauth - django прикол позволяющий изменить базовую модель авторизации. И вообще топ штука
    # https://django-allauth.readthedocs.io/en/latest/installation.html
    # pip install django-allauth
    'allauth',
    'allauth.account',
    # Надстройки allauth для регистрации через соц сети
    'allauth.socialaccount',
    'allauth.socialaccount.providers.telegram',
    'allauth.socialaccount.providers.vk',
    'allauth.socialaccount.providers.yandex',
    # Специальное поле для ввода номеров телефонов
    # pip install django-phonenumber-field
    "phonenumber_field",
]

# Начало настроек django-allauth

# Изменение базовой модели пользователей на определенную
AUTH_USER_MODEL = "c_users.User"

# У пользователей по стандарту определяющим фактором стоит имя, изменяю на email
# ACCOUNT_USER_MODEL_USERNAME_FIELD = 'email'
ACCOUNT_USER_MODEL_USERNAME_FIELD = None

# email - необходим
ACCOUNT_EMAIL_REQUIRED = True

# Имя - нет
ACCOUNT_USERNAME_REQUIRED = False

# Дни на подтверждение email
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1

# Длина имени
ACCOUNT_USERNAME_MAX_LENGTH = 2

# Перенаправление после аутентификации или регистрации
LOGIN_REDIRECT_URL = '/'

# Штучки благодаря которым регистрация заработала
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_UNIQUE_EMAIL = True

# раскомментировать для подтверждения email при регистрации
# ACCOUNT_EMAIL_VERIFICATION = "mandatory" # Не даст зарегаться до подтверждения mail
# Для подтверждения email через email
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'test.email.kaba@gmail.com'
# EMAIL_HOST_PASSWORD = 'Q0000(%kaba%)_'
# DEFAULT_FROM_EMAIL = 'inco.k.b.blizz@gmail.com'

# Для подтверждения email через консоль
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

AUTHENTICATION_BACKENDS = {
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',

    # 'social_core.backends.vk.VKOAuth2',
}

# Для соц сетей
SOCIALACCOUNT_PROVIDERS = {
    'vk': {
        'APP': {
            'client_id': '51639335',
            'secret': 'nJY78btQ0uGjnbm4sugs',
            'key': '74076eb474076eb474076eb4f977149a937740774076eb4105eedf25aa8603bd8867918',
        }
    },
    'telegram': {
        'TOKEN': 'AAGrOLAZ_EJx36ZfCpaDSeXhkqI6rYtA1Qk'
    }
}
# Конец настроек django-allauth 5964658754:AAGrOLAZ_EJx36ZfCpaDSeXhkqI6rYtA1Qk


# Переменная для надстройки 'django.contrib.sites'
SITE_ID = 1
# ACCOUNT_USER_MODEL_USERNAME_FIELD = None
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_USERNAME_REQUIRED = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# время хранения сессии (сейчас == 30 лет) ((60 * 60 * 24 * 30 * 12) *30)
SESSION_COOKIE_AGE = 31104000 * 30


# стабильное кеширование (не сбросит после перезагрузки)
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'


ROOT_URLCONF = 'a_setting.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Добавил пути для шаблонов django-allauth
        'DIRS': [BASE_DIR / 'templates', BASE_DIR / 'templates' / 'account'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'a_setting.wsgi.application'


# # Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = 'ru'

LANGUAGES = (('ru', 'Russian'),)

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# Статистика
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'statics')


# медиа
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'