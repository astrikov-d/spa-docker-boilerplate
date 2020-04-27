# -*- coding: utf-8 -*-
import os

import environ

from conf.apps import *

root = environ.Path(__file__) - 2
env = environ.Env(DEBUG=(bool, False), )
environ.Env.read_env(root('.env'))

DEBUG = env.bool('DEBUG')

SITE_ID = 1

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_ROOT = BASE_DIR

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'www/data')
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'www/static')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_ROOT, 'tpl'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
            'debug': DEBUG
        },
    }
]

ADMINS = ()

MANAGERS = ADMINS

ALLOWED_HOSTS = env('ALLOWED_HOSTS', default=['*'])

TIME_ZONE = 'Asia/Krasnoyarsk'

LANGUAGE_CODE = 'ru'
LANGUAGES = (
    ('ru', 'Russian'),
)

USE_I18N = True

USE_L10N = True

USE_TZ = False

MEDIA_URL = '/data/'

STATIC_URL = '/static/'

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

SECRET_KEY = env('SECRET_KEY')

MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

INSTALLED_APPS = (
                     'django.contrib.humanize',
                     'django.contrib.auth',
                     'django.contrib.admin',
                     'django.contrib.contenttypes',
                     'django.contrib.sessions',
                     'django.contrib.sites',
                     'django.contrib.messages',
                     'django.contrib.staticfiles',
                 ) + THIRD_PARTY_APPS + PROJECT_APPS

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

INTERNAL_IPS = ('127.0.0.1',)

APPEND_SLASH = True

SESSION_SAVE_EVERY_REQUEST = True

ROOT_URLCONF = 'app.urls'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = 'login'

# App specific settings.

APP_URL = env('APP_URL', default='http://localhost')
PORT = int(env('PORT', default=80))
if PORT != 80:
    APP_FULL_URL = f'{APP_URL}:{PORT}'
else:
    APP_FULL_URL = APP_URL

DATABASES = {
    'default': env.db('POSTGRES_URL'),
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache',
    }
}

RAVEN_CONFIG = {
    'dsn': env('RAVEN_DSN', default=''),
    'auto_log_stacks': True,
}

FILE_UPLOAD_PERMISSIONS = 0o644
