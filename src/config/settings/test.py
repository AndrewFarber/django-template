import os

from .base import *



# General
DEBUG = True
ALLOWED_HOSTS = ['*']
SECRET_KEY = os.environ['SECRET_KEY']

# Databases
DATABASES['default']['NAME'] = os.environ['POSTGRES_DB']
DATABASES['default']['USER'] = os.environ['POSTGRES_USER']
DATABASES['default']['PASSWORD'] = os.environ['POSTGRES_PASSWORD']
