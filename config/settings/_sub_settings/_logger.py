# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

import logging.config
from django.utils.log import DEFAULT_LOGGING
from config.settings.base import env

LOGGING_CONFIG = None  # Disable Django's logging setup

LOGLEVEL = env.bool('LOG_LEVEL')

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{asctime} {levelname} {filename} {funcName} {lineno} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{asctime} {levelname} - {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': LOGLEVEL,
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_true'],
            'formatter': 'simple',
        },
        'log_file': {
            'level': LOGLEVEL,
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/api.log',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'verbose',
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/api_error.log',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django_project_api': {
            'handlers': ['console', 'log_file', 'error_file', 'mail_admins'],
            'level': LOGLEVEL,
        },
        'django.request': {
            'handlers': ['mail_admins', 'error_file'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
})
