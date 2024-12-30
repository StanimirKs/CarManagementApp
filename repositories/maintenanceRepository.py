from models.MaintenanceModel import Maintenance
from DTOs.MaintenanceDTO import CreateMaintenanceDTO
from DTOs.ReportDTO import MonthlyRequestsReportDTO
from sqlalchemy.orm import Session


class MaintenanceRepository:
     def __init__(self, db: Session):
          self.db = db

     def getAll(self):
          return self.db.query(Maintenance).all()
     

     def getCar(self, carId: int):
          return self.db.query(Maintenance).filter(Maintenance.carId == carId).all()
     

     def getGarage(self, garageId: int):
          return self.db.query(Maintenance).filter(Maintenance.garageId == garageId).all()
     
     def getDateRange(self, startDate: str, endDate: str):
          return self.db.query(Maintenance).filter(
               Maintenance.scheduledDate >= startDate,
               Maintenance.scheduledDate <= endDate
          ).all()
     
     # Method for filters
     def getFilteredRecords(self, carId=None,garageId=None,startDate=None,endDate=None):
          query = self.db.query(Maintenance)

          # Filter by car
          if carId:
               query = query.filter(Maintenance.carId == carId)
     
          # Filter by garage
          if garageId:
               query = query.filter(Maintenance.garageId == garageId)

          # Filter by date range
          if startDate and endDate:
               query = query.filter(Maintenance.scheduledDate >= startDate, Maintenance.scheduledDate <= endDate)

          return query.all()  
     

     def create(self, createMaintenanceDTO: CreateMaintenanceDTO):
          maintenance = Maintenance(
               carId = createMaintenanceDTO.carId,
               serviceType = createMaintenanceDTO.serviceType,
               scheduledDate = createMaintenanceDTO.scheduledDate,
               garageId = createMaintenanceDTO.garageId
          )
          self.db.add(maintenance)
          self.db.commit()
          self.db.refresh(maintenance)
          return maintenance
     
     def getMonthlyReport(self,garageId, startDate, endDate):
          query = (
               self.db.query(Maintenance)
               .filter(Maintenance.garageId == garageId)
               .filter(Maintenance.scheduledDate >= startDate)
               .filter(Maintenance.scheduledDate <= endDate)
               
          )
          return (query).all()
     

     