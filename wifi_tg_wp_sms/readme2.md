# WiFi Hotspot Auth Service

Сервис авторизации пользователей для общественного WiFi с поддержкой Telegram, WhatsApp и SMS аутентификации.

## Требования

- Docker и Docker Compose
- MikroTik RouterOS 7.x
- VPS с публичным IP

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourrepo/wifi_auth_service.git
   cd wifi_auth_service
   
  
2. Создайте файл .env и заполните настройки:

ini
SECRET_KEY=your-secret-key
DATABASE_URL=mysql://dbuser:dbpass@db/wifi_auth
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
WHATSAPP_API_KEY=your-whatsapp-api-key
SMS_ASSISTENT_API_KEY=your-sms-assistent-api-key
RADIUS_SECRET=your-radius-secret

3.Запустите сервисы:

bash
docker-compose up -d
Примените миграции базы данных:

bash
docker-compose exec web flask db upgrade

Настройка MikroTik
Загрузите скрипт настройки на ваш роутер:

bash
scp mikrotik_scripts/hotspot_setup.rsc admin@your-router-ip:
Выполните скрипт на роутере:

/import hotspot_setup.rsc
Замените <YOUR_VPS_IP> и <RADIUS_SECRET> на реальные значения.

Настройка Grafana
Откройте Grafana в браузере: http://your-vps-ip:3000

Используйте стандартные учетные данные (admin/admin)

Импортируйте дашборд из файла grafana/dashboard.json

Использование
Пользователи могут авторизоваться через:

Telegram (через WebApp)

WhatsApp (получение OTP)

SMS (через сервис SMS Assistent)

Администраторы могут:

Управлять клиентами

Просматривать статистику

Настраивать методы аутентификации

Клиенты могут:

Просматривать свою статистику

Настраивать параметры авторизации

Управлять пользователями

Лицензия
MIT

Это комплексное решение включает все необходимые компоненты для развертывания сервиса авторизации WiFi Hotspot с поддержкой нескольких методов аутентификации, мониторингом через Grafana и интеграцией с MikroTik RouterOS.

 Для полной функциональности необходимо:

Зарегистрировать Telegram бота и получить токен

Создать аккаунт Twilio для WhatsApp интеграции

Настроить SMS Assistent API

Настроить MikroTik для работы с RADIUS

Заполнить все переменные окружения в .env файле

Настроить SSL сертификаты для production окружения
 Для полной функциональности необходимо:

Настроить отношения между моделями в database.py

Добавить обработку форм в контроллерах

Реализовать верификацию OTP кодов

Настроить интеграцию с Telegram WebApp

Добавить обработку ошибок для SMS API

Реализовать пагинацию в таблицах

Настроить права доступа для разных типов пользователей

Добавить валидацию входных данных в формах

Для окончательной настройки:

Создайте базу данных MySQL с указанными параметрами

Настройте переменные окружения в .env

Запустите миграции базы данных

Импортируйте Grafana dashboard

Настройте MikroTik согласно скриптам

Запустите систему через Docker Compose

Система готова к использованию с полным набором функций авторизации, мониторинга и управления.
  
*/   
   Структура проекта
/wifi_auth_service
├── /app
│   ├── /static
│   │   ├── css
│   │   │   └── style.css
│   │   ├── js
│   │   │   ├── auth.js
│   │   │   ├── admin.js
│   │   │   └── client.js
│   │   └── images
│   ├── /templates
│   │   ├── auth.html
│   │   ├── register.html
│   │   ├── client_dashboard.html
│   │   ├── admin_dashboard.html
│   │   └── base.html
│   ├── /controllers
│   │   ├── auth_controller.py
│   │   ├── admin_controller.py
│   │   └── client_controller.py
│   ├── /models
│   │   ├── user.py
│   │   ├── session.py
│   │   └── client.py
│   ├── /services
│   │   ├── telegram_auth.py
│   │   ├── whatsapp_auth.py
│   │   └── sms_auth.py
│   ├── __init__.py
│   ├── config.py
│   └── database.py
├── /mikrotik_scripts
│   ├── hotspot_setup.rsc
│   └── radius_config.rsc
├── /nginx
│   └── wifi_auth.conf
├── /grafana
│   ├── dashboard.json
│   └── provisioning.yaml
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md