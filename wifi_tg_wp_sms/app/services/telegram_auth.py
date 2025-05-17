import requests
import hashlib
import hmac
from app.config import Config

def verify_telegram_auth(data):
    telegram_bot_token = Config.TELEGRAM_BOT_TOKEN
    
    received_hash = data.get('hash')
    auth_data = []
    
    for key in sorted(data.keys()):
        if key != 'hash':
            auth_data.append(f"{key}={data[key]}")
    
    data_check_string = '\n'.join(auth_data)
    secret_key = hashlib.sha256(telegram_bot_token.encode()).digest()
    computed_hash = hmac.new(
        secret_key, 
        msg=data_check_string.encode(), 
        digestmod=hashlib.sha256
    ).hexdigest()
    
    return computed_hash == received_hash