# version 1:
multiples_of_threes = []
for value in list(range(3, 31)):
    MultiplesOfThrees = value * 3
    multiples_of_threes.append(MultiplesOfThrees)
print(multiples_of_threes)

print('\n')

# version 2:
for value in list(range(3, 31)):
    multiples_of_threes = value * 3
    print(multiples_of_threes)