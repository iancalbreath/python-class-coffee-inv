# Mac Littlefield's class
# Ian Calbreath
# Creating modules for the Coffee Management driver program

# This is the module used to search coffee records

def search_coffee():
    # Create a bool variable to use as a flag.
    found = False
    
    # Get the search value.
    search = input('Enter a description to search for: ')
    
    # Open the coffee.txt file.
    coffee_file = open('coffee.txt', 'r')
    
    # Read the first record's description field.
    descr = coffee_file.readline()
    
    # Read the rest of the file.
    while descr != '':
        # Read the quantity field.
        qty = float(coffee_file.readline())
        
        # Strip the new line from the descr
        descr = descr.rstrip('\n')
        
        # Determine whether this record matches the search value
        if descr == search:
            # Display the record.
            print(f'Description: {descr}')
            print(f'Quantity: {qty}')
            print()
            # Set the found flag to True.
            found = True
        
        # Read the next descr
        descr = coffee_file.readline()
        
    # Close the file.
    coffee_file.close()
    
    # If the search value was not found in the file display a message.
    if not found:
        print('That item was not found in the file.')
        
