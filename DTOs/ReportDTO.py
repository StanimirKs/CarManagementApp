class MonthlyRequestsReportDTO:
     def __init__(self, yearMonth: str, requests:int):
          self.yearMonth = yearMonth
          self.requests = requests

     def to_dict(self):
        return {
            'yearMonth': self.yearMonth,
            'requests': self.requests
        }


class GarageDailyAvailabilityReportDTO:
     def __init__(self, date: str, requests: int, availableCapacity: int):
        self.date = date
        self.requests = requests
        self.availableCapacity = availableCapacity
        

 # izpolzva se to_dict za po lesno chetene na dannite
     def to_dict(self):
        return {
            'date': self.date,
            'requests': self.requests,
            'availableCapacity': self.availableCapacity
        }
