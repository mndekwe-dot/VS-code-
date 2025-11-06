class Economy_class_passenger:
    def __init__(self,name,current_location,destination,date):
        self.name = name
        self.current_location = current_location
        self.destination = destination
        self.date = date
    def get_info(self):
        return f"Passenger Name: {self.name}, From: {self.current_location}, To: {self.destination}, Date: {self.date}"
class First_class_Passenger:
    def __init__ (self,name,current_location,destination,date,weight,lounge_access):
        super().__init__(self,name,current_location,destination,date)
        self.weight = weight
        self.lounge_access = lounge_access
    def get_info(self):
        return f"{super.get_info()}, Baggage Weight: {self.weight}kg, Lounge Access: {self.lounge_access}"
class Premium_Passenger:
    def __init__ (self,name,current_location,destination,date,weight,lounge_access,priority_boarding):
        super().__init__(name,current_location,destination,date)
        self.weight = weight
        self.lounge_access = lounge_access
        self.boarding_priority = priority_boarding
    def get_info(self):
        return f"{super.get_info()}, Baggage Weight: {self.weight}kg, Meal Preference: {self.meal_preference}"

Economy1 = Economy_class_passenger("Alice","New York","London","2024-10-01")
First1 = First_class_Passenger("Bob","Los Angeles","Tokyo","2024-11-15",30,True)
Premium1 = Premium_Passenger("Charlie","Chicago","Paris","2024-12-20",25,True)
print(Economy1.get_info())
print(First1.get_info()) 
print(Premium1.get_info())