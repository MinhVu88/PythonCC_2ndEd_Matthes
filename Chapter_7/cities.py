prompt = "\nplz enter the name of a city you've visited or enter 'quit' to exit: "
message = ''

'''
while message != 'quit':
    message = raw_input(prompt)
    if message != 'quit':
        print message
    else:
        break
'''

while True:
    city = input(prompt)
    
    if city == 'quit':
        # use the break statement to exit the while loop immediately without running any remaining code, 
        # regardless of the results of any conditional tests
        break 
    else:
        print (f"\n\tI've been to {city.title()}")