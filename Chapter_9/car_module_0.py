"""A module with multiple classes that can be used to represent a car."""
# you can store as many classes as possible in a module & they should be related to each other
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

class Battery:
    def __init__(self, battery_size=69):
        self.batterySize = battery_size
    
    def describe_battery(self):
        print(f'\nThis car has a {self.batterySize}-kWh battery')
    
    def get_range(self):
        if self.batterySize == 69:
            range = 260
        elif self.batterySize == 100:
            range = 315
        
        print(f'\nThis car can go about {range} miles on a full charge')

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()