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

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'city': self.city,
            'capacity': self.capacity
        }
