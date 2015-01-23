import os
import sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
