"""ASGI config for solusrex project."""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "solusrex.settings")

application = get_asgi_application()
