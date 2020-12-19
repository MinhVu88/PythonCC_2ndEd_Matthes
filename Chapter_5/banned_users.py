# check whether a value is NOT in a list by using the keyword 'not'
banned_users = ['hitler', 'goering', 'eichmann', 'mengele', 'heydrich']
user = 'himmler'
if user not in banned_users:
    print(user.title() + ', you can post a response if you wish')
    