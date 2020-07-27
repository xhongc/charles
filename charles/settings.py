"""
Django settings for charles project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import datetime
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!z+dsq6i#v8z0*$i7=o8^k=+-xa)6+*(hs!4csz3a&sxm_igfl'
WSGI_APPLICATION = 'charles.wsgi.application'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
    'X-CustomAuthHeader',
    'cache-control',
    'content-encoding',
    'p3p',
    'vary',
    'x-msedge-ref'
)
APPEND_SLASH = True
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'project',
    'rest_framework',
    'django_filters',
    'crispy_forms',
    'djcelery',
    'corsheaders',
    'channels',
    'charles.shorturl',
    'charles.chat',
    'charles.blog',
    'charles.comments',
    'xadmin',
    'charles.navi'
]
REST_FRAMEWORK = {
    # 'DEFAULT_FILTER_BACKENDS': (
    #     'django_filters.rest_framework.DjangoFilterBackend',
    # ),
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    #     'rest_framework.authentication.SessionAuthentication',
    #     'rest_framework.authentication.BasicAuthentication',
    # ),
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '30/minute',
        'user': '60/minute'
    },
}
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{asctime} {levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),  # 指明token的有效期
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'project.utils.jwt_response_payload_handler',
}
MIDDLEWARE_CLASSES = ['dwebsocket.middleware.WebSocketMiddleware']
WEBSOCKET_ACCEPT_ALL = True
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.gzip.GZipMiddleware'
]

ROOT_URLCONF = 'charles.urls'
# CACHES = {
#     'default': {
#         'BACKEND':
#             'django.core.cache.backends.locmem.LocMemCache',
#     },
#     'chats': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'cache_table_name',
#         'TIMEOUT': 600,
#         'OPTIONS': {
#             'MAX_ENTRIES': 2000
#         }
#     }
# }
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        'TIMEOUT': 1800,  # 缓存超时时间（默认300，None表示永不过期，0表示立即过期）
        "OPTIONS": {
            "MAX_ENTRIES": 300,  # 最大缓存个数（默认300）
            "CULL_FREQUENCY": 3,  # 缓存到达最大个数之后，剔除缓存个数的比例，即：1/CULL_FREQUENCY（默认3）
            "CLIENT_CLASS": "django_redis.client.DefaultClient",  # redis客户端
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},  # redis最大连接池配置
            "PASSWORD": "",  # redis密码
        },
        'KEY_PREFIX': '',  # 缓存key的前缀（默认空）
        'VERSION': 2,  # 缓存key的版本（默认1）
    },
}
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'blog_tags': 'charles.blog.templatetags.blog_tags',
            }
        },

    },
]

ASGI_APPLICATION = 'charles.routing.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'charles_db',
        'USER': 'root',
        'PASSWORD': 'xhongcc',
        'HOST': 'localhost',
        'PORT': '3306',
    },
}
# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
)
# celery 配置
# python manage.py celery worker --loglevel=info --beat
import djcelery

djcelery.setup_loader()

BROKER_URL = 'redis://localhost:6379/1'  # 代理人
CELERY_RESULT_BACKEND = 'redis://localhost:6379'  # 结果存储地址
CELERY_ACCEPT_CONTENT = ['application/json']  # 指定任务接收的内容序列化类型
CELERY_TASK_SERIALIZER = 'json'  # 任务序列化方式
CELERY_RESULT_SERIALIZER = 'json'  # 任务结果序列化方式
CELERY_TASK_RESULT_EXPIRES = 12 * 30  # 超过时间
CELERY_MESSAGE_COMPRESSION = 'zlib'  # 是否压缩
CELERYD_CONCURRENCY = 4  # 并发数默认已CPU数量定
CELERYD_PREFETCH_MULTIPLIER = 4  # celery worker 每次去redis取任务的数量
CELERYD_MAX_TASKS_PER_CHILD = 3  # 每个worker最多执行3个任务就摧毁，避免内存泄漏
CELERYD_FORCE_EXECV = True  # 可以防止死锁
# CELERY_ENABLE_UTC = False  # 关闭时区
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'  # 定时任务调度器

from celery.schedules import crontab
from celery.schedules import timedelta


CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

# 允许https
SECURE_SSL_REDIRECT = False
