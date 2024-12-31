from repositories.carRepository import carRepository
from DTOs.CarDTO import *

class CarService:
     def __init__ (self, repository: carRepository):
          self.repository = repository
          

     def listCars(self):
          return self.repository.getAll()
     
     def getCar(self, carId: int):
          return self.repository.getById(carId)
     
     def createCar(self,carDTO: CreateCarDTO):
          return self.repository.create(carDTO)
     
     def deleteCar(self, carId: int):
          
          return self.repository.delete(carId)

     def updateCar(self, carId:int, updateCarDTO: UpdateCarDTO):
          car = self.repository.getById(carId)
          if not car:
               raise ValueError("Car not found")
          return self.repository.update(carId, updateCarDTO)

     