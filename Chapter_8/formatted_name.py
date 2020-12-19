# returning a simple value
def get_formatted_name_0(firstName, lastName):
    return f'{firstName} {lastName}'

print(get_formatted_name_0('Adam', 'Jones').title())

'''
- Sometimes it makes sense to make an argument optional 
  so that people using the function can choose to provide extra info only if they want to. 

- You can use default values to make an argument optional
'''
# in this case, the middleName param is assigned a empty default value which can potentially be ignored 
# unless the user provides a value for it
def get_formatted_name_1(firstName, lastName, middleName=''):
    if middleName:
        fullName = f'{firstName} {middleName} {lastName}'
    else:
        fullName = f'{firstName} {lastName}'
    
    return fullName

print(get_formatted_name_1('Maynard', 'Keenan')) # without a middle name

print(get_formatted_name_1('Maynard', 'Keenan', 'James')) # with a middle name (argument order must match the param order)








