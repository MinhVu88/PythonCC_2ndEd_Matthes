'''
- Sometimes you’ll want to spread out your classes over several modules 
  to keep any 1 file from growing too large & avoid storing unrelated classes in the same module. 

- When you store your classes in several modules, you may find that 
  a class in 1 module depends on a class in another module.

- When this happens, you can import the required class into the 1st module
'''

"""A module with multiple classes that can be used to represent electric cars."""
from car_module_1 import Car

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