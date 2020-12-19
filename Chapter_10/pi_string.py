# working with a file's contents
fileName1 = 'Chapter_10/pi_digits.txt'

with open(fileName1) as file_object:
    lines = file_object.readlines()

pi_string1 = ''

for line in lines:
    pi_string1 += line.rstrip()

print(pi_string1)

print(len(pi_string1))

print('----------------------------------------------------------------')

pi_string2 = ''

for line in lines:
    # use strip() to get rid of the whitespace that was on the left side of the digits in each line
    pi_string2 += line.strip() 

print(pi_string2)

print(len(pi_string2))

print('----------------------------------------------------------------')

# working with a large file (a text file that contains pi to 1,000,000 decimal places)
fileName2 = 'Chapter_10/pi_million_digits.txt'

with open(fileName2) as file_object:
    lines = file_object.readlines()

pi_string3 = ''

for line in lines:
    pi_string3 += line.strip()

print(f'{pi_string3[:52]}....') # just print the 1st 50 decimal places

print(len(pi_string3))

print('----------------------------------------------------------------')

# find out if someone’s birthday appears anywhere in the 1st million digits of pi
birthday = input('Enter your birthday (mmddyy): ')

pi_string4 = ''

for line in lines:
    pi_string4 += line.strip()

if birthday in pi_string4:
    print('\n* Your birthday appears in the 1st million digits of pi')
else:
    print('\n* Your birthday does not appear in the 1st million digits of pi')
