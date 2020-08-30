from core.extensions import db


class User(db.Model):
    __tablename__ = 'users'


    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
