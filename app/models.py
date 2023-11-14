from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Result(db.Model):
    __tablename__ = "result"
    id = db.Column(db.Integer,primary_key=True)
    appname = db.Column(db.String(64))
    path  = db.Column(db.String(256))
    method = db.Column(db.String(16))
    params = db.Column(db.Text)
    hash = db.Column(db.String(32))
    date = db.Column(db.Date)
    first_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    repeat_traceid = db.Column(db.String(64))
    old_resp = db.Column(db.Text)
    new_resp = db.Column(db.Text)
    result = db.Column(db.String(1))
    result_detail = db.Column(db.String(256))
    def __repr__(self):
        return "(%s,%s,%s,%s,%s,%s)" %(self.method,self.path,self.params,self.hash,self.first_time,self.update_time)