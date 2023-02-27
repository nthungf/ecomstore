"""
WSGI config for ecomstore project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecomstore.settings')

application = get_wsgi_application()
# application = WhiteNoise(application, root="C:/Users/hung/Documents/PycharmProjects/ecomstore/static")
# application.add_files("/path/to/more/static/files", prefix="more-files/")
