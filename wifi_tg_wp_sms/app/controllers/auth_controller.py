from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.user import User
from app.services.telegram_auth import verify_telegram_auth
from app.services.whatsapp_auth import send_whatsapp_otp
from app.services.sms_auth import send_sms_otp
from app.database import db
from wtforms import Form, StringField, PasswordField, validators


class LoginForm(Form):
    identifier = StringField('Email/Телефон', [validators.required()])
    password = PasswordField('Пароль', [validators.required()])






auth_bp = Blueprint('auth', __name__)

   @auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        
        
        identifier = request.form.get('identifier')
        password = request.form.get('password')
        user = User.query.filter((User.email == identifier) | (User.phone == identifier)).first()
        
        if user and user.check_password(password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('client.dashboard'))
        flash('Неверные учетные данные', 'danger')
         
 
    return render_template('auth.html', form=form)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            user = User(
                username=request.form['username'],
                email=request.form['email'],
                phone=request.form['phone']
            )
            user.set_password(request.form['password'])
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('client.dashboard'))
        except IntegrityError:
            db.session.rollback()
            flash('Пользователь с такими данными уже существует', 'danger')
    return render_template('register.html')

@auth_bp.route('/auth/telegram', methods=['POST'])
def telegram_auth():
    data = request.json
    if verify_telegram_auth(data):
        # Создать сессию
        return {'status': 'success'}
    return {'status': 'error'}

@auth_bp.route('/auth/whatsapp', methods=['POST'])
def whatsapp_auth():
    phone = request.json.get('phone')
    send_whatsapp_otp(phone)
    return {'status': 'otp_sent'}

@auth_bp.route('/auth/sms', methods=['POST'])
def sms_auth():
    phone = request.json.get('phone')
    send_sms_otp(phone)
    return {'status': 'otp_sent
    
    
 

