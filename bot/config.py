# bot/config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
API_BASE_URL = os.getenv('API_BASE_URL', 'http://api:8000')
DEFAULT_LANGUAGE = os.getenv('DEFAULT_LANGUAGE', 'en')
LOCALES_PATH = os.getenv('LOCALES_PATH', '../locales/')
ADMIN_USER_IDS = os.getenv('ADMIN_USER_IDS', '').split(',')

FORCE_SUBSCRIBE_CHANNELS = []  # Will be loaded dynamically from API/Admin Panel

# Add more config as needed
