
from .base import *

DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': env("DB_NAME"),
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env("DB_HOST"),
                'port': int(env("DB_PORT")),
                'username': env("DB_USER"),
                'password': env("DB_PASSWORD"),
                'authSource': "admin"
            }
        }
    }