import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY='fake-key'
INSTALLED_APPS=[
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django_serverside_datatable',
]
DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend'
DEFAULT_INDEX_TABLESPACE=''
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
ALLOWED_HOSTS = ['testserver']