import os
from src.common.env import *

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings.dev')

application = get_asgi_application()
