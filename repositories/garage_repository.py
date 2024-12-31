from sqlalchemy.orm import Session
from models.garage_model import GarageModel
from models.maintenance_model import MaintenanceModel
from DTOs.garage_dto import *
from DTOs.report_dto import GarageDailyAvailabilityReportDTO
import datetime
from sqlalchemy import func


class garageRepository:
     
     def __init__(self, db: Session):
          self.db = db

     def getAll(self):
          garages = self.db.query(GarageModel).all()
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
          garage =  self.db.query(GarageModel).filter(GarageModel.id == garageId).first()
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
          garage = GarageModel(
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


          # vzima danni ot maintenance repoto, puska gi prez DTOto i gi izkarva
     def dailyAvailabilityReport(self, garageId: int, startDate: datetime, endDate: datetime ):
          garage = self.db.query(GarageModel).filter(GarageModel.id == garageId).first()

          if not garage:
               return None
          
          query = (
               self.db.query(
                    MaintenanceModel.scheduledDate.label("date"),
                    func.count(MaintenanceModel.id).label("requests")
                    
               )
               .filter(MaintenanceModel.garageId == garageId)
               .filter(MaintenanceModel.scheduledDate >= startDate)
               .filter(MaintenanceModel.scheduledDate <= endDate).group_by(MaintenanceModel.scheduledDate)
          )
          results = query.all()

          report = []

          for result in results:
               date = result.date
               requests = result.results
               availableCapacity = garage.capacity - requests
               report.append(GarageDailyAvailabilityReportDTO(date, requests, availableCapacity))

          return report  