from core.extensions import db


class Stack(db.Model):
    __tablename__ = 'stack'

    id = db.Column(db.Integer, primary_key=True)

    value = db.Column(db.ARRAY(db.Float))

    def __init__(self, **kwargs):
        super(Stack, self).__init__(**kwargs)

    def get_json(self):
        return {
            "id": self.id,
            "value": self.value
        }
