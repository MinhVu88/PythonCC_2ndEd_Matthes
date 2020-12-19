'''
- Sometimes you’ll want to accept an arbitrary number of arguments 
  but you won’t know ahead of time what kind of info will be passed to the function. 
- In this case, you can write functions that accept as many key-value pairs as the calling statement provides
'''

'''
- 1 example involves building user profiles: you know you’ll get info about a user 
  but you’re not sure what kind of info you’ll receive 

- The function build_profile() in the following example always takes in a 1st & last name 
  but it accepts an arbitrary number of keyword arguments as well

- The double asterisks before the parameter **user_info cause Python to create an empty dictionary called 
  user_info & pack whatever name-value pairs it receives into this dictionary 

- Within the function, you can access the key-value pairs in user_info just as you would for any dictionary 
'''
def build_profile(firstName, lastName, **user_info):
    user_info['first_name'] = firstName

    user_info['last_name'] = lastName

    return user_info

user_profile = build_profile('Nikola', 'Tesla',
                             age=86,
                             field='Electrical & Mechanical engineering',
                             project='Alternating current')

for k, v in user_profile.items():
    print(f'{k}: {v}')
