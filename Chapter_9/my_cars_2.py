# importing a module into a module, also using aliases
from car_module_1 import Car as C
from electric_car_module import ElectricCar as EC

car1 = C('bentley', 'flying spur', 2019)

print(car1.get_name())

car2 = EC('tesla', 'model s', 2019)

print(car2.get_name())