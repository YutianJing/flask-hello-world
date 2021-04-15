from db import db
class userdb(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(64),unique=True,index=True)

    def __init__(self,username):
        self.username = username

    def __repr__(self):
        return "<user %r>"%self.username
