from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.db_utils import db
from flask_sqlalchemy import SQLAlchemy



class Car(db.Model):
     __tablename__ = "car"
     id = db.Column(db.Integer, primary_key=True)
     make = db.Column(db.String(30), nullable=False)
     model = db.Column(db.String(50), nullable=False)
     productionYear = db.Column(db.Integer, nullable=False)
     licensePlate = db.Column(db.String(20), nullable=True, unique=True)
     
     # handles the relationship to the maintenance table
     maintenance = db.relationship('maintenance', back_populates='car')


     def __repr__(self):
          return f'<CarModel {self.name}>'