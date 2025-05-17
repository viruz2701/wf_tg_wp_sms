from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from app.models import User, Client, Session
from app.database import db
from datetime import datetime, timedelta

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.before_request
@login_required
def check_admin():
    if not current_user.is_admin:
        flash('Доступ запрещен', 'danger')
        return redirect(url_for('auth.login'))

@admin_bp.route('/dashboard')
def dashboard():
    clients = Client.query.all()
    users = User.query.count()
    active_sessions = Session.query.filter(Session.end_time == None).count()
    return render_template('admin_dashboard.html', 
                         clients=clients,
                         total_users=users,
                         active_sessions=active_sessions)

@admin_bp.route('/clients')
def clients():
    clients = Client.query.all()
    return render_template('admin_clients.html', clients=clients)

@admin_bp.route('/sessions')
def sessions():
    page = request.args.get('page', 1, type=int)
    sessions = Session.query.order_by(Session.start_time.desc()).paginate(page=page, per_page=20)
    return render_template('admin_sessions.html', sessions=sessions)

@admin_bp.route('/users')
def users():
    users = User.query.all()
    return render_template('admin_users.html', users=users)