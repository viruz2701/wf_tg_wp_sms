from app.database import db

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    mikrotik_ip = db.Column(db.String(15))
    hotspot_name = db.Column(db.String(50))
    telegram_auth_enabled = db.Column(db.Boolean, default=False)
    whatsapp_auth_enabled = db.Column(db.Boolean, default=False)
    sms_auth_enabled = db.Column(db.Boolean, default=False)
    sms_api_key = db.Column(db.String(100))
    sms_sender_name = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    sessions = db.relationship('Session', backref='client', lazy=True)