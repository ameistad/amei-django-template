# -*- coding: utf-8 -*-
# Production settings
# https://docs.djangoproject.com/en/stable/howto/deployment/checklist/

from .base import *  # noqa

DEBUG = False

# Custom admin url
ADMIN_URL = env('DJANGO_ADMIN_URL')

# Allowed hosts
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['{{ cookiecutter.domain_name }}'])

# Gunicorn WSGI HTTP Server.
INSTALLED_APPS += ('gunicorn', )

# Simplified static file serving with whitenoise.
# https://warehouse.python.org/project/whitenoise/
WHITENOISE_MIDDLEWARE = ['whitenoise.middleware.WhiteNoiseMiddleware', ]
MIDDLEWARE = WHITENOISE_MIDDLEWARE + MIDDLEWARE
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Email
DEFAULT_FROM_EMAIL = env('DJANGO_DEFAULT_FROM_EMAIL',
                         default='{{ cookiecutter.repo_name }} <noreply@{{ cookiecutter.domain_name }}>')

# INSTALLED_APPS += ("anymail", )
# ANYMAIL = {
#     "MAILGUN_API_KEY": env('DJANGO_MAILGUN_API_KEY'),
# }
# EMAIL_BACKEND = "anymail.backends.mailgun.MailgunBackend"
