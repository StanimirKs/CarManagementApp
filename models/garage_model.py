from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from database.db_utils import db

# syzdava tablicata chrez migracii
class GarageModel(db.Model):
     __tablename__ = 'garage'
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(100), nullable=False, unique=True)
     location = db.Column(db.String(100), nullable=False)
     city = db.Column(db.String(100), nullable=False)
     capacity = db.Column(db.Integer(), nullable=False)

     # handles the relationship
     maintenanceRelationship = db.relationship('MaintenanceModel', backref='garage_relation')


