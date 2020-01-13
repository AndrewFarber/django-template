from .base import *
from .base import env


# Inherit env file settings
env.read_env(env_file=str(ENV_DIR('.django')))
env.read_env(env_file=str(ENV_DIR('.postgres')))

# General
DEBUG = True
ALLOWED_HOSTS = ['*']
SECRET_KEY = env.str('SECRET_KEY')

# Databases
DATABASES['default']['NAME'] = env.str('POSTGRES_DB')
DATABASES['default']['USER'] = env.str('POSTGRES_USER')
DATABASES['default']['PASSWORD'] = env.str('POSTGRES_PASSWORD')
DATABASES['default']['HOST'] = env.str('POSTGRES_HOST')
DATABASES['default']['PORT'] = env.int('POSTGRES_PORT')
