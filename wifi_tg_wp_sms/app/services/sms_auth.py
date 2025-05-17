import requests
from app.config import Config
from sqlalchemy import text

def send_sms_otp(phone):
    # Использование параметризованных запросов
    stmt = text("SELECT * FROM users WHERE phone = :phone")
    user = db.session.execute(stmt, {'phone': phone}).fetchone()
    
def send_sms_otp(phone, client=None):
    url = "https://dev.sms-assistent.by/api-plain-zapros-dlya-otpravki-sms"
    
    payload = {
        'user': client.sms_api_key if client else Config.SMS_ASSISTENT_API_KEY,
        'recipient': phone,
        'message': f'Ваш код для авторизации: {generate_otp()}',
        'sender': client.sms_sender_name if client else 'WiFiAuth'
    }
    
    response = requests.get(url, params=payload)
    return response.status_code == 200

def generate_otp():
    import random
    return str(random.randint(1000, 9999))