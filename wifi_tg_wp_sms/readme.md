# Сервис авторизации WiFi Hotspot

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Полное решение для управления авторизацией в публичных WiFi-сетях с поддержкой Telegram, WhatsApp и SMS. Включает веб-интерфейс, аналитику и интеграцию с MikroTik.

## 📋 Требования

- Сервер Ubuntu 22.04 LTS
- Docker 20.10+
- Docker Compose 2.12+
- Git
- Python 3.9+
- MySQL клиент
- Nginx
- Certbot (Let's Encrypt)

## 🚀 Быстрый старт

### 1. Установка зависимостей

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y docker.io docker-compose git python3 python3-pip mysql-client nginx certbot
sudo systemctl enable docker
2. Клонирование репозитория
bash
git clone https://github.com/yourrepo/wifi_auth_service.git
cd wifi_auth_service
3. Настройка окружения
bash
cp .env.example .env
nano .env  # Заполните реальными значениями
Пример .env:

ini
SECRET_KEY=your-secret-key-here
DATABASE_URL=mysql://dbuser:dbpass@db/wifi_auth
TELEGRAM_BOT_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
SMS_ASSISTENT_API_KEY=your-sms-key
4. Запуск контейнеров
bash
docker-compose up -d --build
5. Миграции базы данных
bash
docker-compose exec web flask db init
docker-compose exec web flask db migrate -m "Initial"
docker-compose exec web flask db upgrade
6. Настройка MikroTik
Загрузите скрипты на роутер:

bash
scp mikrotik_scripts/*.rsc admin@your-router-ip:
Выполните на роутере:

bash
/import hotspot_setup.rsc
/import radius_config.rsc
7. Настройка домена и SSL
Создайте Nginx конфиг:

bash
sudo nano /etc/nginx/sites-available/wifi-auth
Вставьте конфигурацию:

nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /grafana/ {
        proxy_pass http://localhost:3000/;
        proxy_set_header Host $host;
    }
}
Включите конфиг и получите SSL:

bash
sudo ln -s /etc/nginx/sites-available/wifi-auth /etc/nginx/sites-enabled/
sudo certbot --nginx -d your-domain.com
8. Настройка Grafana
Откройте http://your-domain.com/grafana

Логин: admin/admin (смените пароль)

Импортируйте дашборд из grafana/dashboard.json

🛠 Использование системы
Для администраторов:
Доступ к /admin после входа

Управление клиентами и пользователями

Просмотр общей статистики

Настройка глобальных параметров

Для клиентов:
Личный кабинет на /client

Настройка методов авторизации

Просмотр статистики трафика

Управление сессиями пользователей

Для пользователей WiFi:
Captive Portal с выбором метода входа

SMS/Telegram/WhatsApp аутентификация

Контроль времени сессии и трафика

🔧 Устранение неполадок
Проблема: Не работает подключение к базе данных
Решение: Проверьте:

bash
docker-compose logs db
mysql -u dbuser -p -h 127.0.0.1 wifi_auth
Проблема: Не отправляются SMS
Решение: Убедитесь что:

Указан правильный API ключ в .env

Баланс на счету SMS провайдера

Роутер пропускает трафик на dev.sms-assistent.by

Проблема: Ошибки миграций
Решение: Выполните:

bash
docker-compose exec web flask db stamp head
docker-compose exec web flask db migrate
docker-compose exec web flask db upgrade
📄 Лицензия
MIT License. Подробности в файле LICENSE.

📧 Поддержка
По вопросам настройки и проблемам обращайтесь:
support@yourdomain.com
Telegram: @wifi_support_bot

