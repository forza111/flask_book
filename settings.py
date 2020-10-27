import os

import secrets


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = 'yEe5JjegFnuxdh}3ZSM9'
HOST = '0.0.0.0'
PORT = 5000
HOSTNAME = f'http://{HOST}:{PORT}'

MONGODB_SETTINGS = {
    'db': os.getenv('MONGODB_NAME', 'flaskbook'),
    'host': os.getenv('MONGODB_HOST', 'db'),
    'port': os.getenv('MONGODB_PORT', 27017)
}

