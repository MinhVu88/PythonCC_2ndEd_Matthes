# importing multiple classes from the module, separate them with commas
from car_module_0 import Car, ElectricCar

car1 = Car('volkswagen', 'beetle', 2019)

print(car1.get_name())

car2 = ElectricCar('tesla', 'model y', 2019)

print(car2.get_name())