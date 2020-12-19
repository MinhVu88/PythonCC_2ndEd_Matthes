# make a list of the 1st 10 number numbers (1 - 10) using 2 asterisks (**) to represent exponents

# version 1:
squares_0 = []
for number in range(1, 11):
    square_numbers = number ** 2
    
    squares_0.append(square_numbers)

print(squares_0)

print('\n')

# version 2:
squares_1 = []
for number in range(10, 21):
    squares_1.append(number**2)

print(squares_1)

print('\n')

# version 3: a list comprehension combines the for loop & the creation of new elements into 1 line & automatically appends each new element
squares_2 = [value ** 2 for value in range(1, 11)]

print(squares_2)