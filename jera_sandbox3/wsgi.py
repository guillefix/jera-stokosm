"""
WSGI config for jera_sandbox3 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jera_sandbox3.settings")

application = get_wsgi_application()

application = DjangoWhiteNoise(application)

#from dj_static import Cling

#application = Cling(get_wsgi_application())
