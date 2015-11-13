"""
Django settings for proffesionalweekend project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lnc1mnyakp6yr=pui-v2)pdo7*3e36!i05dwyrq$1xx$ynse7-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'flat',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize', 

    # MAIN APPS
    'vblog',
    'the_don',
    'journey',

    # 3RD-PARTY APPS
    'registration',
    'ckeditor',
    'crispy_forms',
    'disqus',
    'django_social_share',
    'watson',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'proffesionalweekend.urls'

# DJANGO REGISTRATION SETTING
LOGIN_REDIRECT_URL = '/journey/'
ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = True # Automatically log the user in.


# DISQUS SETTING
DISQUS_API_KEY = 'kELez10djkJnl2b3BPy3BRQFrFbtdqwp5cdpA4YrwSzujzXei8UcGVuqUDPYPTjF'
DISQUS_WEBSITE_SHORTNAME = 'pewe'

# CKEDITOR SETTING
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['codesnippet', 'codesnippetgeshi'],
            ['RemoveFormat', 'Source']
        ],
        # 'extraPlugins': ','.join([
        #     'codesnippet',
        # ]),
           'height': 400,
           'width': 600,
    }
}

CRISPY_TEMPLATE_PACK = 'bootstrap3'
CRISPY_CLASS_CONVERTERS = {'textinput': "form-control input-lg"}

# EMAIL SERVER SETTING
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.yahoo.com'
EMAIL_HOST_USER = 'peweofficial@yahoo.com'
EMAIL_HOST_PASSWORD = 'Nallaismystar!!!'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'peweofficial@yahoo.com'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'proffesionalweekend.wsgi.application'

AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.RemoteUserBackend',
        'django.contrib.auth.backends.ModelBackend',
)

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db-pw.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'proweekendDB',
#         'USER': 'zea',
#         'PASSWORD': 'root',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '/home/zea/Riset/Django-Project/proffesionalweekend_env/proffesionalweekend/static',
)
STATIC_URL = '/static/'

MEDIA_ROOT = '/home/zea/Riset/Django-Project/proffesionalweekend_env/proffesionalweekend/media'
MEDIA_URL = '/vblog/media/'

CKEDITOR_UPLOAD_PATH = 'media/uploads/'
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
