fav_places = {'jack': ['osaka', 'tokyo', 'shanghai'],
              'tim': ['new york', 'oxford'],
              'layne': ['berlin']}

for name, places in fav_places.items():
    print('\n' + name.title() + "'s fav places:")
    for place in places:
        if len(places) == 1:
            print('\t' + name.title() + ' has only 1 fav place: ' + place.title())
        else:
            print('-  ' + place.title())
        