"""A module with a single class that can be used to represent a car."""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 
    
    def get_name(self):
        return f'\n{self.year} {self.make.title()} {self.model.title()}'
    
    def read_odometer(self):
        return f'\nThis {self.model.title()} {self.make.title()} has {self.odometer_reading} miles on it'
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("\n\tYou can't roll back an odometer")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles