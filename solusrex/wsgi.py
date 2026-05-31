"""WSGI config for solusrex project."""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "solusrex.settings")

application = get_wsgi_application()
