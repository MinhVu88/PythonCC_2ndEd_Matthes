# using a function with a while loop
def get_formatted_name(firstName, lastName):
    return f'{firstName} {lastName}'

while True:
    print("\nPlz tell me your name or enter 'q' to quit: ")
    
    first_name = input('\n\tYour 1st name: ')

    if first_name == 'q': break

    last_name = input('\n\tYour last name: ')

    if last_name == 'q': break

    print(f'\n* Hello {get_formatted_name(first_name, last_name)}!')