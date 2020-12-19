cities = {'tokyo': {'country': 'japan', 
                    'population': 9999, 
                    'fact': 'the capital & biggest city of japan'},
          
          'berlin': {'country': 'germany', 
                     'population': 6000000, 
                     'fact': 'the capital city of germany'},
          
          'new york': {'country': 'the us', 
                       'population': 123456, 
                       'fact': 'the biggest city in the us'}
         }

for city, city_info in cities.items():
    print(city.title() + ':')
    
    country = city_info['country']
    pop = city_info['population']
    fact = city_info['fact']
    
    print('\tCountry: ' + country.title() + ' - Population: ' + str(pop) + ' - Fact: ' + fact)