''' Dice: 
- Make a class Die with 1 attribute called sides, which has a default value of 6.
- Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. 
- Make a 6-sided die and roll it 10 times.
- Make a 10-sided die and a 20-sided die. Roll each die 10 times
'''
from random import randint

class Die:
    def __init__(self):
        self.sides = 6
    
    def roll_die(self):
        return randint(1, self.sides)
        
die1 = Die()

round1 = 1

while round1 <= 10:
    print(f"\n- Round #{round1}: The die's value -> {die1.roll_die()}")
    round1 += 1

print('\n--------------------------------')

die2 = Die()

die2.sides = 10

round2 = 1

while round2 <= 10:
    print(f"\n- Round #{round2}: The die's value -> {die2.roll_die()}")
    round2 += 1

print('\n--------------------------------')

die3 = Die()

die3.sides = 20

round3 = 1

while round3 <= 10:
    print(f"\n- Round #{round3}: The die's value -> {die3.roll_die()}")
    round3 += 1
