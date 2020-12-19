multiples_of_ten = input('enter a number: ')
multiples_of_ten = int(multiples_of_ten)

if multiples_of_ten % 10 == 0:
    print (str(multiples_of_ten) + ' is a multiple of 10')
else:
    print (str(multiples_of_ten) + ' is not a multiple of 10')