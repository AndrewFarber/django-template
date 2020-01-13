import os
import sys


if __name__ == '__main__':

    try:
        from config.settings.base import APPS_DIR
    except ImportError:
        raise ImportError('Could not import APPS_DIR')

    try:
        from django.core.management import execute_from_command_line
        from django.conf import settings
    except ImportError:
        try:
            import django
            
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                'available on your PYTHONPATH environment variable? Did you '
                'forget to activate a virtual environment?'
            )

        raise

    sys.path.append(APPS_DIR)
    execute_from_command_line(sys.argv)
