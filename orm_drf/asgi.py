"""
ASGI config for orm_drf project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more inform_drfation on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_drf.settings")

application = get_asgi_application()
