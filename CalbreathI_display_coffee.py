# Mac Littlefield's class
# Ian Calbreath
# Creating modules for the Coffee Management driver program

# This is the module used to display all coffee records

def display_coffee():
    # Open the coffee.txt file.
    coffee_file = open('coffee.txt', 'r')
    
    # Read the first record's description field.
    descr = coffee_file.readline()
    
    # Read the rest
    while descr != '':
        # Read the quantity field
        qty = float(coffee_file.readline())
        
        # Strip the new line
        descr = descr.rstrip('\n')
        
        # Display the record.
        print(f'Description: {descr}')
        print(f'Quantity: {qty}')
        
        # Read the next descr
        descr = coffee_file.readline()
        
    # Close the file
    coffee_file.close()