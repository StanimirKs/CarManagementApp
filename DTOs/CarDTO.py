class CreateCarDTO:
     def __init__(self,carId: int, make: str, model: str, productionYear: int, licencePlate: str, garageIds: list):
          self.carId = carId
          self.make = make
          self.model = model
          self.productionYear = productionYear
          self.licensePlate = licencePlate
          self.garageIds = garageIds

class UpdateCarDTO:
    def __init__(self, make: str, model: str, productionYear: int, licensePlate: str, garageIds: list):
        self.make = make
        self.model = model
        self.productionYear = productionYear
        self.licensePlate = licensePlate
        self.garageIds = garageIds

class ResponseCarDTO:
    def __init__(self, id: int, make: str, model: str, productionYear: int, licensePlate: str, garages: list):
        self.id = id
        self.make = make
        self.model = model
        self.productionYear = productionYear
        self.licensePlate = licensePlate
        self.garages = garages

 # metoda prevryshta dannite v dictionary
    def to_dict(self):
        return {
            'id': self.id,
            'make': self.make,
            'model': self.model,
            'productionYear': self.productionYear,
            'licensePlate': self.licensePlate,
            'garages': self.garages
        }