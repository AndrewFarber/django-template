import os
import sys

import environ


# Names
ENV_DIR_NAME = 'env'
APPS_DIR_NAME = 'apps'
CONFIG_DIR_NAME = 'config'


# Directories
BASE_DIR = (environ.Path(__file__) - 4)
ROOT_DIR = (environ.Path(__file__) - 3)
ENV_DIR = ROOT_DIR.path(ENV_DIR_NAME)
APPS_DIR = ROOT_DIR.path(APPS_DIR_NAME)
CONFIG_DIR = ROOT_DIR.path(CONFIG_DIR_NAME)


# Environment
env = environ.Env()


# General
DEBUG = False
USE_TZ = True
USE_L10N = True
USE_I18N = True
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
WSGI_APPLICATION = 'config.wsgi.application'


# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'ATOMIC_REQUESTS': True,
    }
}


# URLs
ROOT_URLCONF = 'config.urls'


# Apps
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
]
LOCAL_APPS = [
]
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS


# Security
# X_FRAME_OPTIONS = 'DENY'
# CSRF_COOKIE_HTTPONLY = True
# SESSION_COOKIE_HTTPONLY = True
# SECURE_BROWSER_XSS_FILTER = True


# Passwords
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# Static
STATIC_URL = '/static/'
STATIC_ROOT = str(ROOT_DIR('staticfiles'))
STATICFILES_DIRS = [str(APPS_DIR.path('static'))]


# Media
MEDIA_URL = '/media/'
MEDIA_ROOT = str(APPS_DIR('media'))


# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(APPS_DIR.path('templates'))],
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
