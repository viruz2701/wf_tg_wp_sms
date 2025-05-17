from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from app.models import Client, Session
from app.database import db
from datetime import datetime, timedelta

client_bp = Blueprint('client', __name__, url_prefix='/client')

@client_bp.before_request
@login_required
def check_client_access():
    pass  # Добавить проверку прав доступа

@client_bp.route('/dashboard')
def dashboard():
    client = Client.query.filter_by(owner_id=current_user.id).first()
    sessions = Session.query.filter_by(client_id=client.id).order_by(Session.start_time.desc()).limit(10)
    
    stats = {
        'today': Session.query.filter(
            Session.client_id == client.id,
            Session.start_time >= datetime.now() - timedelta(hours=24)
        ).count(),
        'total': Session.query.filter_by(client_id=client.id).count(),
        'active': Session.query.filter(
            Session.client_id == client.id,
            Session.end_time == None
        ).count()
    }
    
    return render_template('client_dashboard.html', 
                          client=client,
                          sessions=sessions,
                          stats=stats)

@client_bp.route('/settings', methods=['GET', 'POST'])
def settings():
    client = Client.query.filter_by(owner_id=current_user.id).first()
    
    if request.method == 'POST':
        client.hotspot_name = request.form.get('hotspot_name')
        client.mikrotik_ip = request.form.get('mikrotik_ip')
        client.sms_api_key = request.form.get('sms_api_key')
        client.sms_sender_name = request.form.get('sms_sender_name')
        db.session.commit()
        flash('Настройки успешно обновлены', 'success')
    
    return render_template('client_settings.html', client=client)