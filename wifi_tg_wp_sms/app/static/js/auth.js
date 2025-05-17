document.addEventListener('DOMContentLoaded', function() {
    const authMethod = document.querySelector('#auth_method');
    const telegramAuth = document.querySelector('#telegram_auth');
    const whatsappAuth = document.querySelector('#whatsapp_auth');
    const smsAuth = document.querySelector('#sms_auth');
    
    authMethod.addEventListener('change', function() {
        telegramAuth.style.display = 'none';
        whatsappAuth.style.display = 'none';
        smsAuth.style.display = 'none';
        
        if (this.value === 'telegram') {
            telegramAuth.style.display = 'block';
            initTelegramAuth();
        } else if (this.value === 'whatsapp') {
            whatsappAuth.style.display = 'block';
        } else if (this.value === 'sms') {
            smsAuth.style.display = 'block';
        }
    });
    
    function initTelegramAuth() {
        // Инициализация Telegram WebApp
        if (window.Telegram && Telegram.WebApp) {
            Telegram.WebApp.ready();
            Telegram.WebApp.expand();
        }
    }
    
    document.querySelector('#whatsapp_send').addEventListener('click', function() {
        const phone = document.querySelector('#whatsapp_phone').value;
        fetch('/auth/whatsapp', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({phone: phone})
        }).then(response => response.json())
          .then(data => {
              if (data.status === 'otp_sent') {
                  alert('Код отправлен на WhatsApp');
              }
          });
    });
    
    document.querySelector('#sms_send').addEventListener('click', function() {
        const phone = document.querySelector('#sms_phone').value;
        fetch('/auth/sms', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({phone: phone})
        }).then(response => response.json())
          .then(data => {
              if (data.status === 'otp_sent') {
                  alert('Код отправлен по SMS');
              }
          });
    });
});