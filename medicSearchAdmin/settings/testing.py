from .settings import *

SECRET_KEY = '$%$#%gdjkkaHHD5Ggd55HSH56lfpçq00Lmdfand4q9o0ui8DPÇOJsdS5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'dbTest.sqlite3',
    }
}
