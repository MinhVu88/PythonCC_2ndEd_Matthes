''' Cities: 
- Write a function called describe_city() that accepts the name of a city and its country. 
- The function should print a simple sentence, such as Reykjavik is in Iceland. 
- Give the parameter for the country a default value. 
- Call your function for 3 different cities, at least 1 of which is not in the default country
'''
def describe_city(name, country='Germany'):
    print(f'\n{name.title()} is in {country.title()}')

describe_city('Münster')

describe_city('Bielefeld')

describe_city(name='Kyoto', country='Japan')
