"""
WSGI config for todo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()



# virtenv = os.environ['APPDIR'] + '/virtenv/'
virtenv = os.path.join(os.environ.get('OPENSHIFT_PYTHON_DIR','.'), 'virtenv')
os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib/python2.7/site-packages')
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except:
    pass
 
# new codes we adding for Django
import django.core.handlers.wsgi
 
os.environ['DJANGO_SETTINGS_MODULE'] = os.environ['OPENSHIFT_APP_NAME']+'.settings'
sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', os.environ['OPENSHIFT_APP_NAME']))
application = django.core.handlers.wsgi.WSGIHandler()
