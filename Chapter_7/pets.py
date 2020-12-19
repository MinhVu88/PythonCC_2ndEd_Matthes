# removing all instances of specific values from a list
pets = ['dog', 'spider', 'hamster', 'lizard', 'spider', 'goldfish', 'cat', 'pig', 'spider', 'bird',
         'scorpion', 'snake', 'turtle', 'spider', 'hedgehog', 'fox', 'monkey', 'skunk', 'wallaby', 'spider']

print (pets)

print ('\n')

''' 
in pets, there are multiple instances of the value 'spider' 
to remove all those instances, use a while loop & the remove() function learned in chapter 3 (Introducing lists)
'''

while 'spider' in pets:
    pets.remove('spider')

print (pets)