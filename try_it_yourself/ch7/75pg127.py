prompt = 'enter your age: '
active = True

while active:
    age = input(prompt)
    age = int(age)
    
    if age <= 3:
        price = 0
        active = False
    elif age <= 12:
        price = 10
        active = False
    else:
        price = 15
        active = False
    
    print ("\nif you're " + str(age) + ' years old. Then you will be charged $' + str(price))