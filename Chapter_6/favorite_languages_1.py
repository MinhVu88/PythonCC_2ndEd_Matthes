# loop thru all key-value pairs by using the items() method
fav_languages = {
    'layla': 'python',
    'dan': 'swift',
    'keith': 'c++',
    'erica': 'java',
    'julia': 'javascript',
    'mary': 'python'
    }

for name, language in fav_languages.items():
    print('\n' + name.title() + "'s favorite language is " + language.upper())

print('\n')

# loop thru all the keys in a dic by using the keys() method
friends = ['keith', 'julia']

for name in fav_languages.keys():
    print(name.title())
    if name in friends:
        print('\thi ' + name.title() + ', you like ' + fav_languages[name].title() + ", don't you?")

if 'luke' not in fav_languages.keys():
    print('\nLuke, plz choose your favorite language')

print('\n')

# return the items in a dic by using the sorted() function
for name in sorted(fav_languages.keys()):
    print('\n' + name.title() + ', thanks for picking a language to learn')

print('\n')

# loop thru all the values in a dic by using the values() method
print('the favorite languages:')

for language in fav_languages.values():
    print('-  ' + language.title())

print('\n')

# eliminate duplicate values by using the set() function
print('the favorite languages without duplicate values:')

for language in set(fav_languages.values()):
    print('+  ' + language.title())