from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from sqlalchemy import  DateTime

db = SQLAlchemy()

class Blacklist(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(128))
    app_uuid = db.Column(db.String(128))
    blocked_reason = db.Column(db.String(128))
    ip = db.Column(db.String(128))
    createdAt = db.Column(DateTime)

class BlackListSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Blacklist
        include_relationships = True
        load_instance = True

