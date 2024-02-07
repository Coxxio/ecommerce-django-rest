import os
from src.common.env import *

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings.dev')

application = get_wsgi_application()
