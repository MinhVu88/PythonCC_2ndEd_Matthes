from name_function_0 import get_formatted_name

while True:
    firstName = input("\nEnter your 1st name or 'q' to quit: ")

    if firstName == 'q':
        break

    lastName = input("\nEnter your last name or 'q' to quit: ")

    if lastName == 'q':
        break

    print(f'\n- Your name: {get_formatted_name(firstName, lastName)}')