import os
import sys

from django.core.wsgi import get_wsgi_application

from .settings.base import APPS_DIR


sys.path.append(str(APPS_DIR))
application = get_wsgi_application()
