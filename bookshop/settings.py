"""
Django settings for bookshop project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0(+ua9d)*wki)4y$ru2&_*dg4qcik@@%0ejsm_=-us7j6jw$)3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

#AUTHENTICATION_BACKENDS = (
    #'django.contrib.auth.backends.ModelBackend', # necessary for django.auth
    #'survey.modelbackend.EmailBackend' # custom backend to authenticate using the email field
#)

#test email link in terminal

#EMAIL_HOST      = 'localhost'
#EMAIL_HOST_PASSWORD = ''
#EMAIL_HOST_USER = ''
#EMAIL_PORT      = 1025
#EMAIL_USE_TLS   = False
#DEFAULT_FROM_EMAIL = 'webmaster@localhost'
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#send email for forgot password 

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'username@gmail.com'
EMAIL_HOST_PASSWORD = 'password'
DEFAULT_FROM_EMAIL = 'sanuptpm20@gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'





INSTALLED_APPS = (
    
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'book',
    'django.contrib.admin',
    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'bookshop.urls'


LOGIN_REDIRECT_URL ='/users/account/'

LOGIN_URL = '/users/login/'

LOGOUT_URL = '/users/logout/'

STATIC_ROOT = '/home/saju/bookshop/book/static/'#for photo upload

STATIC_URL = '/static/'

WSGI_APPLICATION = 'bookshop.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

MEDIA_ROOT = '/home/saju/bookshop/media/'#for photo upload

MEDIA_URL = '/media/'#for photo upload

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


