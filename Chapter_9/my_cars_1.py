# importing the entire module
# accessing the classes in the module: module_name.class_name
import car_module_0

car1 = car_module_0.Car('toyota', 'yaris', 2019)

print(car1.get_name())

car2 = car_module_0.ElectricCar('tesla', 'roadster', 2019)

print(car2.get_name())

# importing all classes from a module (not recommended): from module_name import *