"""
Django settings for example project.

Generated by 'django-admin startproject' using Django 2.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django import __version__ as django_version

if float(django_version[0:3]) >= 4.0:
    from django.utils.translation import gettext_lazy as _
else:
    from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6c$f^^c^44lxq5_vn3s%)uy#%ovzc!k))(a(h1_b2%$(ohit+f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'admin_shortcuts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'example'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'example.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + "/templates"],
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

WSGI_APPLICATION = 'example.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'


# Admin Shortcuts

ADMIN_SHORTCUTS = [
    {
        'shortcuts': [
            {
                'url': '/',
                'open_new_window': True,
            },
            {
                'url_name': 'admin:logout',
            },
            {
                'title': 'Users',
                'url_name': 'admin:auth_user_changelist',
                'count': 'example.utils.count_users',
            },
            {
                'title': 'Groups',
                'url_name': 'admin:auth_group_changelist',
                'count': 'example.utils.count_groups',
                'has_perms': ['example.change_group', 'example.delete_group'],
            },
            {
                'title': 'Add user',
                'url_name': 'admin:auth_user_add',
                'test_func': 'example.utils.has_perms_to_users',
            },
        ]
    },
    {
        'title': 'CMS',
        'shortcuts': [
            {
                'title': 'Pages',
                'url_name': 'admin:index',
            },
            {
                'title': 'Files',
                'url_name': 'admin:index',
            },
            {
                'title': 'Contact forms',
                'icon': 'columns',
                'url_name': 'admin:index',
                'count_new': '3',
                'count_alert': '5',
                'count_total': '5',
                'count_active': '25',
            },
            {
                'title': 'Products',
                'url_name': 'admin:index',
            },
            {
                'title': _('Orders'),
                'url_name': 'admin:index',
                'count_new': '12',
                'count_alert': '5',
                'count_active': '25',
            },
        ]
    },
]
ADMIN_SHORTCUTS_SETTINGS = {
    'show_on_all_pages': True,
    'hide_app_list': True,
    'open_new_window': False,
}
