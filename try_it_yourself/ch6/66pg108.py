fav_languages = {
    'luke': 'python',
    'dave': 'swift',
    'ken': 'c++',
    'eric': 'java',
    'jane': 'javascript'
    }

friends = ['liam', 'dave', 'lauren', 'ian', 'eric', 'wayne']

for friend in friends:
    if friend in fav_languages.keys():
        print('\tthanks ' + friend.title() + ' for taking the poll')
    else:
        print(friend.title() + ', plz take the poll')