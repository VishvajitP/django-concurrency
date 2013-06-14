import os

DEBUG = True
STATIC_URL = '/static/'
AUTHENTICATION_BACKENDS = ('demoproject.backends.AnyUserBackend',)

SITE_ID = 1
ROOT_URLCONF = 'demoproject.urls'
SECRET_KEY = ';klkj;okj;lkn;lklj;lkj;kjmlliuewhy2ioqwjdkh'
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'concurrency',
    # 'demoproject.demoapp'
)

TEMPLATE_DIRS = ['demoproject/templates']
from demoproject.settings_sqlite import *  # NOQA

db = os.environ.get('DBENGINE', None)
if db:
    mod = __import__('demoproject.settings_%s' % db, fromlist=['demoproject'])
    DATABASES = mod.DATABASES