import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql://user:password@localhost/wifi_auth')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    WHATSAPP_API_KEY = os.getenv('WHATSAPP_API_KEY')
    SMS_ASSISTENT_API_KEY = os.getenv('SMS_ASSISTENT_API_KEY')
    GRAFANA_URL = os.getenv('GRAFANA_URL', 'http://localhost:3000')
    RADIUS_SECRET = os.getenv('RADIUS_SECRET', 'radiussecret')