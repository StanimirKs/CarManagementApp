from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from database.db_utils import db


# syzdava tablicata chrez migracii
class MaintenanceModel(db.Model):
     __tablename__ = 'maintenance'
     id = db.Column(Integer,primary_key=True)
     carId = db.Column(db.Integer,db.ForeignKey('car.id'), nullable=False)
     garageId = db.Column(db.Integer,db.ForeignKey('garage.id'), nullable=False)
     serviceType = db.Column(db.String(100), nullable=False)
     scheduledDate = db.Column(db.Date, nullable=False)
     garageName = db.Column(db.String(100), nullable=False)


     # relationships
     car= db.relationship('car', back_populates='maintenance')
     garage = db.relationship('garage', back_populates='maintenance')

     