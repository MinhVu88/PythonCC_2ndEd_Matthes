fav_numbers = {'jake': [47, 85, 88], 
               'liam': [18, 96, 32], 
               'colin': [25, 51, 29], 
               'sarah': [69, 15, 21, 67], 
               'kate': [13, 34]}

for name, numbers in fav_numbers.items():
    print(name.title() + "'s fav numbers:")
    for no in numbers:
        print('\t- ' + str(no))