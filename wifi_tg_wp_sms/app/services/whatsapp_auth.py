from twilio.rest import Client
from app.config import Config
import random

twilio_client = Client(Config.WHATSAPP_API_KEY)

def send_whatsapp_otp(phone):
    otp = str(random.randint(1000, 9999))
    message = f"Ваш код авторизации: {otp}"
    
    try:
        twilio_client.messages.create(
            body=message,
            from_='whatsapp:+14155238886',  # Twilio sandbox number
            to=f'whatsapp:{phone}'
        )
        return True
    except Exception as e:
        print(f"WhatsApp send error: {e}")
        return False