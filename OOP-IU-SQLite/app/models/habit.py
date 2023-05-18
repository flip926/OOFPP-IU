from app import db
from datetime import datetime


class Habit(db.Model):
    id = db.Column(db.Integer,nullable=False,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    periodicity = db.Column(db.String(10),nullable=False)
    streak = db.Column(db.Integer,default=0)
    times_broken=db.Column(db.Integer,default=0)
    date_time = db.Column(db.DateTime,index=True,default=datetime.utcnow)

    def __repr__(self):
        return f"{self.name},{self.date_time},{self.streak}"
    