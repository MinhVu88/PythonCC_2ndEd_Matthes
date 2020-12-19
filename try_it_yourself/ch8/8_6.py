''' City Names: 
- Write a function called city_country() that takes in the name of a city and its country. 
- The function should return a string formatted like this: "Santiago, Chile"
- Call your function with at least 3 city-country pairs and print the values that are returned
'''
def city_country(city, country):
    return f'{city.title()}, {country.title()}'

print(city_country('Dortmund', 'Germany'))

print(city_country('Düsseldorf', 'Germany'))

print(city_country('Tokyo', 'Japan'))
