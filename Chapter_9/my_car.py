# importing a single class from the module
from car_module_0 import Car

new_car = Car('ferrari', 'f8 spider', 2019)

print(new_car.get_name())

new_car.odometer_reading = 27

print(new_car.read_odometer())
