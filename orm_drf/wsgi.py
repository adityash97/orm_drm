"""
WSGI config for orm_drf project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more inform_drfation on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_drf.settings")

application = get_wsgi_application()
