from sqlalchemy.orm import Session
from models.CarModel import Car
from DTOs.CarDTO import *

class carRepository:
     def __init__(self,db: Session):
          self.db = db

     def getAll(self):
          cars = self.db.query(Car).all()
     # izpolzva se list comprehension 
          responseDTOList = [
               ResponseCarDTO(
                    id=car.id,
                    make = car.make,
                    model = car.model,
                    productionYear = car.productionYear,
                    licensePlate = car.licensePlate,
                    garages = car.garages
               )for car in cars
          ]
          return [dto.to_dict() for dto in responseDTOList]
     
     def getById(self,carId: int):
          car = self.db.query(Car).filter(Car.id == carId).first()
          if not car : return None

          response = ResponseCarDTO(
               id = car.id,
               make = car.make,
               model = car.model,
               productionYear = car.productionYear,
               licensePlate = car.licensePlate,
               garages = car.garages
          )
          return response.to_dict()
     
     def create(self, CreateCarDTO:CreateCarDTO):
          car = Car(
               carId = CreateCarDTO.carId,
               make = CreateCarDTO.make,
               model = CreateCarDTO.model,
               productionYear = CreateCarDTO.productionYear,
               licensePlate = CreateCarDTO.licensePlate,
               garages = CreateCarDTO.garageIds
          )
          self.db.add(car)
          self.db.commit()
          self.db.refresh(car)
          return car
     
     def update(self,carId: int, updateCarDTO: UpdateCarDTO):
          car = self.getById(carId)
          if not car:
               return None
          
           #? vars calls the __dict__ method
          for key, value in vars(updateCarDTO).items():         
               setattr(car, key, value)


          self.db.commit()
          self.db.refresh(car)
          return car
          
     def delete(self, carId: int):
          car = self.getById(carId)
          if car:
               self.db.delete(car)
               self.db.commit()
          return car

