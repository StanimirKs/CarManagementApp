from datetime import date

class CreateMaintenanceDTO:
    def __init__(self, carId: int, serviceType: str, scheduledDate: date, garageId: int):
        self.carId = carId
        self.serviceType = serviceType
        self.scheduledDate = scheduledDate
        self.garageId = garageId

class UpdateMaintenanceDTO:
    def __init__(self, carId: int, serviceType: str, scheduledDate: date, garageId: int):
        self.carId = carId
        self.serviceType = serviceType
        self.scheduledDate = scheduledDate
        self.garageId = garageId

class ResponseMaintenanceDTO:
    def __init__(self, id: int, carId: int, car_name: str, serviceType: str, scheduledDate: date, garageId: int, garage_name: str):
        self.id = id
        self.carId = carId
        self.car_name = car_name
        self.serviceType = serviceType
        self.scheduledDate = scheduledDate
        self.garageId = garageId
        self.garage_name = garage_name

    def to_dict(self):
        return {
            'id': self.id,
            'carId': self.carId,
            'carName': self.car_name,
            'serviceType': self.serviceType,
            'scheduledDate': str(self.scheduledDate),
            'garageId': self.garageId,
            'garageName': self.garage_name
        }
