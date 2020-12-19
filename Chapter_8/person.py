# returning a dictionary
def build_person_0(firstName, lastName):
    return {'first_name': firstName, 'last_name': lastName}

print(build_person_0('Justin', 'Chancellor'))

'''
- the build_person_1() function's definition contains a new optional param named age

- age is assigned None (a special value that's used when a variable has no specific values assigned to it)

- Think of None as a placeholder value

- In conditional tests, None evaluates to false
'''
def build_person_1(firstName, lastName, age=None):
    person = {'first_name': firstName, 'last_name': lastName}

    if age:
        person['age'] = age
    
    return person

# because the function call includes a value for age, so that value is stored in the dictionary
print(build_person_1('Danny', 'Carey', age=59))
















