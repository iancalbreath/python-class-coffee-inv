import CalbreathI_coffee_records
import CalbreathI_display_coffee
import CalbreathI_search_coffee
import CalbreathI_modify_coffee
import CalbreathI_delete_coffee

ADD_COFFEE_CHOICE = 1   # Defining global constants for choices (add function)
DISPLAY_COFFEE_CHOICE = 2  #  display function
SEARCH_COFFEE_CHOICE = 3  #  search function
MODIFY_COFFEE_CHOICE = 4  #  modify function
DELETE_COFFEE_CHOICE = 5  #  delete function
QUIT_CHOICE = 6         #  quit function

def funcionInicial():
    choice = 0
    while choice != QUIT_CHOICE:
        display_menu()
        choice = int(input('Enter your choice: '))
        if choice == ADD_COFFEE_CHOICE:
            CalbreathI_coffee_records.add_coffee()  # Calling the function to add coffee from the imported module
        elif choice == DISPLAY_COFFEE_CHOICE:
            CalbreathI_display_coffee.display_coffee()
        elif choice == SEARCH_COFFEE_CHOICE:
            CalbreathI_search_coffee.search_coffee()
        elif choice == MODIFY_COFFEE_CHOICE:
            CalbreathI_modify_coffee.modify_coffee()
        elif choice == DELETE_COFFEE_CHOICE:
            CalbreathI_delete_coffee.delete_coffee()
        elif choice == QUIT_CHOICE:
            print('Exiting the program...')
        else:
            print('Error: invalid selection.')

def display_menu():
    print(' IAN CALBREATH COFFEE MANAGEMENT MENU')
    print('1) Add more Coffee Choices to List')
    print('2) Display all the Coffee choices')
    print('3) Search Coffee Choices')
    print('4) Modify Coffee Choices')
    print('5) Delete a Coffee Choice')
    print('6) Quit')