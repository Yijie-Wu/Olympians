from datetime import datetime

from app.extensions import db


class Auth(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    nt = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(256))
    password_hash = db.Column(db.String(256))
    last_login = db.Column(db.DateTime, default=datetime.utcnow)
    avatar_s = db.Column(db.String(256))
    avatar_m = db.Column(db.String(256))
    avatar_l = db.Column(db.String(256))
    avatar_row = db.Column(db.String(256))


