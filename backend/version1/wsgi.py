"""
WSGI config for version1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""


import os
import sys

from django.core.wsgi import get_wsgi_application

proj = os.path.dirname(__file__)
projs = os.path.dirname(proj)
if projs not in sys.path:
    sys.path.append(proj)
    sys.path.append(projs)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "version1.settings")
application = get_wsgi_application()