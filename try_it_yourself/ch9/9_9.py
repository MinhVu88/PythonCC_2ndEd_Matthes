''' Battery Upgrade: 
- Use the final version of electric_car.py from this section. 
- Add a method to the Battery class called upgrade_battery(). 
- This method should check the battery size and set the capacity to 100 if it isn’t already. 
- Make an electric car with a default battery size, call get_range() once and then 
  call get_range() a 2nd time after upgrading the battery. 
- You should see an increase in the car’s range
'''
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # a default value
        self.fuel_gauge = ''
    
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
    
    def fill_gas_tank(self, gas):
        if gas <= 0:
            self.fuel_gauge = 'Empty'
            return self.fuel_gauge
        else:
            self.fuel_gauge = 'Not Empty'
            return self.fuel_gauge

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
    
    def upgrade_battery(self):
        if self.batterySize == 69:
           self.batterySize = 100
           print('\n\t* Upgraded the battery to 100 kwh')
        else:
           print('\n\t* The battery has already been upgraded') 
            
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def describe_battery(self):
        print(f'\nThis {self.make.title()} has a {self.battery_size}-kwh battery')
    
    def fill_gas_tank(self):
        print(f"\nElectric cars, such as {self.make.title()}, don't need gas/fuel to operate")

ec = ElectricCar('tesla', 'roadster', 2019)

print(ec.get_name())

ec.battery.describe_battery() # check the car's current battery

ec.battery.get_range() # check the car's current range

# upgrade the battery & check it out
ec.battery.upgrade_battery()

ec.battery.describe_battery()

ec.battery.get_range()

# upgrading & checking again
ec.battery.upgrade_battery()

ec.battery.describe_battery()

ec.battery.get_range()
