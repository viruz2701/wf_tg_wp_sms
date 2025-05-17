from app.database import db
from datetime import datetime

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    internal_ip = db.Column(db.String(15))
    mac_address = db.Column(db.String(17))
    hostname = db.Column(db.String(100))
    start_time = db.Column(db.DateTime, default=datetime.utcnow)
    end_time = db.Column(db.DateTime)
    data_used = db.Column(db.BigInteger, default=0)
    auth_method = db.Column(db.String(20))

    def calculate_duration(self):
        if self.end_time:
            return self.end_time - self.start_time
        return datetime.utcnow() - self.start_time

    def format_data_used(self):
        if self.data_used > 1024**3:
            return f"{self.data_used/1024**3:.2f} GB"
        return f"{self.data_used/1024**2:.2f} MB"