from .base import *
from .base import env

import django_heroku

django_heroku.settings(locals())
