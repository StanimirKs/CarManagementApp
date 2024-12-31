from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.db_utils import db
from flask_sqlalchemy import SQLAlchemy
from models.maintenance_model import MaintenanceModel
from models.garage_model import GarageModel


# syzdava tablicata chrez migracii
class Car(db.Model):
     __tablename__ = "car"
     
     id = db.Column(db.Integer, primary_key=True)
     make = db.Column(db.String(30), nullable=False)
     model = db.Column(db.String(50), nullable=False)
     productionYear = db.Column(db.Integer, nullable=False)
     licensePlate = db.Column(db.String(20), nullable=True, unique=True)
     
     # handles the relationship to the maintenance table
     maintenanceRelationship = db.relationship('MaintenanceModel', backref='car_relation',lazy=True)
     garages = db.relationship('GarageModel',secondary='car_garage', backref='cars')



     def __repr__(self):
          return f'<CarModel {self.make} {self.model}>'