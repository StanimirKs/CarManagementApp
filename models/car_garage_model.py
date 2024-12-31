from sqlalchemy import Table, Column, Integer, ForeignKey,UniqueConstraint
from database.db_utils import db


car_garage = Table('car_garage', db.Model.metadata,
    Column('carId', Integer, ForeignKey('car.id'), nullable=False),
    Column('garageId', Integer, ForeignKey('garage.id'), nullable=False),
    # The primary key is implicitly the combination of car_id and garage_id
    # No need to define primary_key=True here for association tables
    UniqueConstraint('carId', 'garageId', name='uix_car_garage')
)
