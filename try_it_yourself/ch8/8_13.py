''' User Profile: 
- Start with a copy of user_profile.py 
- Build a profile of yourself by calling build_profile(), 
  using your 1st and last names and 3 other key-value pairs that describe you
'''
def build_profile(firstName, lastName, **profile):
    profile['first_name'] = firstName

    profile['last_name'] = lastName

    return profile

myProfile = build_profile('Maynard', 'Keenan',
                           age=55,
                           occupation='vocalist',
                           band='Tool')

for k, v in myProfile.items(): print(f'- {k}: {v}')
