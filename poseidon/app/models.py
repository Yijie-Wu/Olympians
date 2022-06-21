from datetime import datetime

from app.extensions import db



class FileManager(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    # 文件原始名称
    file_oname = db.Column(db.String(256))
    #
    file_fname = db.Column(db.String(256), unique=True)
    file_size = db.Column(db.Float, default=0)
    uploader_name = db.Column(db.String(50))
    uploader_email = db.Column(db.String(256))
    upload_time = db.Column(db.DateTime, default=datetime.utcnow)
    # if True, the upload file name must unique
    file_oname_only = db.Column(db.Boolean, default=False)
    meta = db.Column(db.Text, default='{}')


