# importing another class from the module
from car_module_0 import ElectricCar

my_ec = ElectricCar('tesla', 'model x', 2019)

print(my_ec.get_name())

my_ec.battery.describe_battery()

my_ec.battery.get_range()