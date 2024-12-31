class CreateGarageDTO:
    def __init__(self,garageId: int, name: str, location: str, city: str, capacity: int):
        self.garageId = garageId
        self.name = name
        self.location = location
        self.city = city
        self.capacity = capacity

class UpdateGarageDTO:
    def __init__(self, name: str, location: str, city: str, capacity: int):
        self.name = name
        self.location = location
        self.city = city
        self.capacity = capacity

class ResponseGarageDTO:
    def __init__(self, id: int, name: str, location: str, city: str, capacity: int):
        self.id = id
        self.name = name
        self.location = location
        self.city = city
        self.capacity = capacity

 # izpolzva se to_dict za po lesno chetene na dannite
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'city': self.city,
            'capacity': self.capacity
        }
