import os
import sys
import traceback

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
from django.test import RequestFactory

# Ensure project root is on sys.path (so 'config' can be imported)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

django.setup()

# Force DEBUG True for local diagnostic so template errors raise and show tracebacks
from django.conf import settings as _dj_settings
try:
    _dj_settings.DEBUG = True
except Exception:
    pass

# Force DEBUG True for local diagnostic so template errors raise and show tracebacks
from django.conf import settings as _dj_settings
try:
    _dj_settings.DEBUG = True
except Exception:
    pass

from mixes.views import home_page_view

rf = RequestFactory()
request = rf.get('/')

# If you need a user on the request, attach an AnonymousUser by default
from django.contrib.auth.models import AnonymousUser
request.user = AnonymousUser()

try:
    response = home_page_view(request)
    print('Response type:', type(response))
    try:
        # If it's an HttpResponse, print status code and a short content preview
        print('Status code:', response.status_code)
        content = response.content.decode('utf-8')
        print('Content preview (first 500 chars):')
        print(content[:500])
    except Exception as e:
        print('Could not decode response content:', e)
except Exception:
    print('Exception while rendering home_page_view:')
    traceback.print_exc()
    sys.exit(1)
