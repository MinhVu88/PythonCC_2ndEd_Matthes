''' Inheritance:
- You don’t always have to start from scratch when writing a class. 

- If the class you’re writing is a specialized version of another class you wrote, you can use inheritance. 

- When 1 class inherits from another, it takes on the attributes and methods of the 1st class. 

- The original class is called superclass and the new class is subclass. 

- The subclass can inherit any or all of the attributes and methods of its superclass 
  but it’s also free to define new attributes and methods of its own
'''

# Car is the superclass of ElectricCar
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

car = Car('volkswagen', 'beetle', 2019)

car.fill_gas_tank(0)

print(f"\n{car.make}'s current amount of fuel is {car.fuel_gauge}")

car.fill_gas_tank(1)

print(f"\n{car.make}'s current amount of fuel is {car.fuel_gauge}")

# ElectricCar1 is a sub-class of Car
class ElectricCar1(Car):
    """ initialize the superclass's attributes """
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

        """ initialize an attribute specific to the subclass """
        self.battery_size = 23
    
    """ define a method specific to the subclass """
    def describe_battery(self):
        print(f'\nThis {self.make.title()} has a {self.battery_size}-kwh battery')
    
    """ override fill_gas_tank() from Car """
    def fill_gas_tank(self):
        print(f"\nElectric cars, such as {self.make.title()}, don't need gas/fuel to operate")

ec1 = ElectricCar1('tesla', 'model x', 2019)

print(ec1.get_name())

ec1.describe_battery()

ec1.fill_gas_tank()

''' Instances as attributes:
- When modeling something from the real world in code, 
  you may find that you’re adding more and more detail to a class. 

- You’ll find that you have a growing list of attributes and 
  methods and that your files are becoming lengthy. 
  
- In these cases, you might recognize that part of 1 class can be written as a separate class. 

- You can break your large class into smaller classes that work together

- For example, if we continue adding detail to the ElectricCar class, 
  then obviously we’re adding many attributes and methods specific to the car’s battery. 

- When this happens, we can stop & move those attributes & methods to a separate class called Battery. 

- Then we can use a Battery instance as an attribute in the ElectricCar class
'''
class Battery:
    """ battery_size is an optional param whose value will be set to 69 if no arg is provided """
    def __init__(self, battery_size=69):
        self.batterySize = battery_size
    
    def describe_battery(self):
        print(f'\nThis car has a {self.batterySize}-kWh battery')
    
    """ now we can describe the battery in detail without cluttering ElectricCar2 """
    def get_range(self):
        if self.batterySize == 69:
            range = 260
        elif self.batterySize == 100:
            range = 315
        
        print(f'\nThis car can go about {range} miles on a full charge')

class ElectricCar2(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

        """ assign a Battery instance (with a default size of 69) to the attribute """
        """ whenever __init__() is called, any ElectricCar2 instance will have a Battery instance created automatically """
        self.battery = Battery()
    
    def describe_battery(self):
        print(f'\nThis {self.make.title()} has a {self.battery_size}-kwh battery')
    
    def fill_gas_tank(self):
        print(f"\nElectric cars, such as {self.make.title()}, don't need gas/fuel to operate")

ec2 = ElectricCar2('tesla', 'roadster', 2019)

print(ec2.get_name())

ec2.battery.describe_battery()

ec3 = ElectricCar2('tesla', 'model y', 2019)

print(ec3.get_name())

ec3.battery.get_range()
