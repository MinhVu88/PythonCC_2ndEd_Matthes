# an if-elif-else statement
age_0 = 12

if age_0 < 4:
    price = 0
elif age_0 < 18:
    price = 5
else:
    price = 10

print('your admission cost is $' + str(price))

print('\n')

# it's possible to use multiple elif blocks

age_1 = 73

if age_1 < 4:
    price = 5
elif age_1 < 18:
    price = 10
elif age_1 < 65:
    price = 20
else:
    price = 0

print('your admission cost is $' + str(price))    

print('\n')

# or omit the else block
age_2 = 33

if age_2 < 4:
    price = 5
elif age_2 < 18:
    price = 10
elif age_2 < 65:
    price = 20
elif age_2 >= 65:
    price = 0
    
print('your admission cost is $' + str(price))