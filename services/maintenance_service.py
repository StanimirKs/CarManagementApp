from repositories.maintenance_repository import MaintenanceRepository
from DTOs.maintenance_dto import *
from DTOs.report_dto import MonthlyRequestsReportDTO
import datetime

class MaintenanceService:
     def __init__(self, repository: MaintenanceRepository):
          self.repository = repository

# vadi vsichki zapisi, kato gi pravi v dictionary
     def listAll(self):
          maintenances = self.repository.getAll()
          return [ResponseMaintenanceDTO(vars(**maintenances)) for singleMaintenance in maintenances]

     def getFilteredMaintenance(self, carId=None, garageId=None, startDate=None, endDate=None):
          newRecords = self.repository.getFilteredRecords(carId,garageId,startDate,endDate)

          if not newRecords:
               return " No records found for provided filter! Try again"

          return [
               ResponseMaintenanceDTO(
                    id=record.id,
                    carId = record.carId,
                    serviceType=record.serviceType,
                    scheduledDate=record.scheduledDate,
                    garageId=record.garageId
               ) for record in newRecords
          ]
     
     def createMaintenance(self, createDTO: CreateMaintenanceDTO):
          return self.repository.create(createDTO)
     
     def getMonthlyReport(self,garageID:int,startDate:datetime,endDate:datetime):
          newReport = self.repository.getMonthlyReport(garageID,startDate,endDate)

          if not newReport:
               return "No report entry found! Please check data"

          return[
               MonthlyRequestsReportDTO(
                    date = entry.date,
                    requestsNum = entry.requests,
                    availableCapacity = entry.availableCapacity
               ) for entry in newReport
          ]