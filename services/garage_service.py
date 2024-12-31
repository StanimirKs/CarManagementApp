from repositories.garageRepository import garageRepository
from DTOs.GarageDTO import *
import datetime

# 
class GarageService:
     def __init__ (self, repository: garageRepository):
          self.repository = repository

     def listGarages(self):
          return self.repository.getAll()
     
     def getGarage(self, garageId: int):
          return self.repository.getById(garageId)
     
     def dailyAvailabilityReport(self, garageId: int, startDate: datetime, endDate: datetime):
          report = self.repository.dailyAvailabilityReport(garageId,startDate,endDate)
          if not report: return None
          return report
     
     def createGarage(self, garageDTO : CreateGarageDTO):
          return self.repository.create(garageDTO)
     
     # vzima danni ot DTO
     def updateGarage(self, garageId: int, updateGarageDTO: UpdateGarageDTO):
          garage = self.repository.getById(garageId)
          if not garage:
               raise ValueError("Garage not found")
          return self.repository.update(garageId, updateGarageDTO)
     
     def deleteGarage(self, garageId: int):
          return self.repository.delete(garageId)