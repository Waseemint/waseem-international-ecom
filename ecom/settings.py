import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
# SECRET_KEY = os.environ.get('SECRET_KEY')
SECRET_KEY = 'dsds!@#$232143'
DEBUG = True
ALLOWED_HOSTS = [
    'https://waseemint.com/',
    'waseemint.com',
    'waseem-int-d368a88e8f0a.herokuapp.com',
    'www.waseemint.com',
    '127.0.0.1'
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "corsheaders",
    'category',
    'accounts',
    'store',
    'carts',
    'orders',
    'customkit',
    'images',
    'youtube',
    'ads',
    'widget_tweaks',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_session_timeout.middleware.SessionTimeoutMiddleware",
]

SESSION_EXPIRE_SECONDS = 36000
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
CORS_ALLOWED_ORIGINS = [
    "https://waseemint.com",
    "http://waseemint.com",
    "https://www.waseemint.com",
    # Add other domains as needed
]
CORS_ALLOW_CREDENTIALS = True  # Allows cookies to be sent with requests
CORS_ALLOW_METHODS = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
CORS_ALLOW_HEADERS = ['accept', 'accept-encoding', 'authorization', 'content-type', 'dnt', 'origin', 'user-agent', 'x-csrftoken', 'x-requested-with']


ROOT_URLCONF = 'ecom.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "category.context_processors.categories_processor",
                "carts.context_processors.counter",
                "store.context_processors.products",
                "customkit.context_processors.footer_links",
                "customkit.context_processors.base_tags",
                "customkit.context_processors.main_logoo",
                
            ],
        },
    },
]

WSGI_APPLICATION = 'ecom.wsgi.application'
AUTH_USER_MODEL = "accounts.Account"

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.environ.get('NAME'),
#         'USER': os.environ.get('USER'),
#         'PASSWORD': os.environ.get('DB_PASSWORD'),
#         'HOST': os.environ.get('HOST'),
#         'PORT': '5432',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Karachi'
USE_I18N = True
USE_TZ = True

# # AWS S3 Settings for Media Files Only
# AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
# AWS_S3_FILE_OVERWRITE = False
# AWS_DEFAULT_ACL = None

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Local Storage Settings for Static Files
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

ADMINS = [
    ('Waseem Ahmed', 'waseemint.pk@gmail.com'),
]
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.ERROR: "danger",
}

# Email Configuration
# DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_EMAIL')
DEFAULT_FROM_EMAIL = 'test.webcog@gmail.com'
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'test.webcog@gmail.com'
EMAIL_HOST_PASSWORD = 'ljglguxixgtizmbx'
# EMAIL_HOST_USER = os.environ.get('DEFAULT_EMAIL')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_SECURE = False
