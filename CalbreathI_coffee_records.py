# Mac Littlefield's Class
# Ian Calbreath
# Re-writing program 6-15.  We need a module containing a function that will be used in IanCalbreath-Hwrk6.py

# This program adds coffee inventory records to the coffee.txt file.

def add_coffee():
    # Create a variable to control the loop.
    another = 'y'
    
    # Open coffee.txt in append mode.
    coffee_file = open('coffee.txt', 'a')

    # Add records to the file.
    while another == 'y' or another == 'Y':
        # Get the coffee record data.
        print('Enter the following coffee data: ')
        descr = input('Description: ')
        qty = float(input('Quantity (in pounds): '))
        
        # Append the data to the file.
        coffee_file.write(descr + '\n')
        coffee_file.write(str(qty) + '\n')
        
        # Determine whether the user wants to add another record
        print('Do you want to add another record?')
        another = input('Y = yes, anything else = no: ')
    
    # Close the file.
    coffee_file.close()
    print('Data appended to coffee.txt.')


