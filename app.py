import os

# List of restaurants with name, category, and active status
restaurants = [
    {'name': 'Sushito', 'category': 'Japanese', 'active': True},
    {'name': 'Nono Ludovico', 'category': 'Pizza', 'active': False},
]

def clear():
    """Clears the console for compatibility with different operating systems."""
    os.system('clear' if os.name == 'posix' else 'cls')

def clear_message(message):
    """Clears the console and prints a message."""
    clear()
    print(message)
    print()

def return_to_menu():
    """Waits for user input before returning to the main menu."""
    print()
    input("Press any key to return to the main menu.")
    main()

def display_program_name():
    """Displays the program name in a stylized font."""
    print('''
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█\n''')

def display_options():
    """Displays the menu options to the user."""
    print('1. Register restaurant')
    print('2. List restaurants')
    print('3. Activate restaurant')
    print('4. Exit\n')

def finalize_app():
    """Finalizes the app with a message."""
    clear_message('Finalizing the app')

def invalid_option():
    """Informs the user of an invalid option and returns to the menu."""
    clear_message('Invalid option!')
    return_to_menu()

def register_new_restaurant():
    """Registers a new restaurant."""
    clear_message('Registering new restaurants')
    restaurant_name = input('Enter the name of the restaurant you want to register: ')
    category = input(f'Enter the category of the restaurant {restaurant_name}: ')
    restaurant_data = {'name': restaurant_name, 'category': category, 'active': False}
    restaurants.append(restaurant_data)
    print(f'The restaurant {restaurant_name} has been successfully registered.')

    return_to_menu()

def list_restaurants():
    """Lists all registered restaurants."""
    clear_message('Listing restaurants')

    for restaurant in restaurants:
        name = restaurant['name']
        category = restaurant['category']
        active = 'Active' if restaurant['active'] else 'Inactive'
        print(f'- {name} | {category} | {active}')

    return_to_menu()

def toggle_restaurant_state():
    """Toggles the active state of a specified restaurant."""
    clear_message('Changing restaurant state')
    restaurant_name = input('Enter the name of the restaurant you want to change the state of: ')
    restaurant_found = False

    for restaurant in restaurants:
        if restaurant_name == restaurant['name']:
            restaurant_found = True
            restaurant['active'] = not restaurant['active']
            message = f'The restaurant {restaurant_name} has been successfully activated.' if restaurant['active'] else f'The restaurant {restaurant_name} has been successfully deactivated.'
            print(message)
            break

    if not restaurant_found:
        print('The restaurant was not found.')

    return_to_menu()

def choose_option():
    """Allows the user to choose an option from the menu."""
    try:
        option_chosen = int(input('Choose an option: '))

        if option_chosen == 1:
            register_new_restaurant()
        elif option_chosen == 2:
            list_restaurants()
        elif option_chosen == 3:
            toggle_restaurant_state()
        elif option_chosen == 4:
            finalize_app()
        else:
            invalid_option()
    except ValueError:
        invalid_option()

def main():
    """Main function to run the program."""
    clear()
    display_program_name()
    display_options()
    choose_option()

if __name__ == '__main__':
    main()
