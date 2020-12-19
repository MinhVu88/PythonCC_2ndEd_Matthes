fav_languages = {
    'layla': ['python', 'go'],
    'dan': ['swift', 'objective c'],
    'keith': ['c++'],
    'erica': ['java', 'c'],
    'julia': ['javascript', 'r'],
    'mary': ['c#', 'python']
    }

print("our friends' fav languages:\n")

for name, languages in fav_languages.items():
    print(name.title() + ':')
    for language in languages:
        if len(languages) == 1:
            print('\t' + name.title() + ' has only 1 fav language: ' + language.title())
        else:
            print('\t- ' + language.title())