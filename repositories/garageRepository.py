from sqlalchemy.orm import Session
from models.GarageModel import Garage
from DTOs.GarageDTO import *


class garageRepository:
     
     def __init__(self, db: Session):
          self.db = db

     def getAll(self):
          garages = self.db.query(Garage).all()
          responseDTOList = [
               ResponseGarageDTO(
                    id = garage.id,
                    name = garage.name,
                    location = garage.location,
                    city = garage.city,
                    capacity = garage.capacity
               ) for garage in garages
          ]
          return [dto.to_dict() for dto in responseDTOList]
          
               
          
     
     def getById(self, garageId: int):
          garage =  self.db.query(Garage).filter(Garage.id == garageId).first()
          if not garage :
               return None
          
          response = ResponseGarageDTO(
               id = garage.id,
               name = garage.name,
               location = garage.location,
               city = garage.city,
               capacity = garage.capacity
          )
          return response.to_dict()
     
     def create(self,createGarageDTO: CreateGarageDTO):
          garage = Garage(
               garageId = createGarageDTO.garageId,
               name = createGarageDTO.name,
               location = createGarageDTO.location,
               city = createGarageDTO.city,
               capacity = createGarageDTO.capacity
          )


          self.db.add(garage)
          self.db.commit()
          self.db.refresh(garage)
          return garage
     
     def update(self, garageId: int, updateGarageDTO: UpdateGarageDTO):
          garage = self.getById(garageId)
          if not garage:
               return None
          
          for key, value in vars(updateGarageDTO).items():
               setattr(garage, key, value)


          self.db.commit()
          self.db.refresh(garage)
          return garage
     
     def delete(self, garageId:int):
          garage = self.getById(garageId)
          if garage:
               self.db.delete(garage)
               self.db.commit()

          return garage
