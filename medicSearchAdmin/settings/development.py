from .settings import *
import json

with open(BASE_DIR / 'dBase/pass.json') as file:
    BASICS = json.load(file)

SECRET_KEY = BASICS['SECRET_KEY']

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': BASICS['DBNAME'],
        'USER': BASICS['DBUSER'],
        'PASSWORD': BASICS['DBPASSWORD'],
        'HOST': BASICS['DBHOST'],
        'PORT': BASICS['DBPORT']
    }
}
