rivers = {'danube': 'germany',
          'thames': 'england',
          'indus': 'tibet'}

for river, country in rivers.items():
    print('\nThe ' + river.title() + ' river runs thru ' + country.title())

print('\nThe names of the rivers:')
for river in rivers.keys():
    print('\t' + river.title())

print('\nThe countries the rivers run thru:')
for country in rivers.values():
    print('\t' + country.title())