# Mac Littlefield's class
# Ian Calbreath
# Creating modules for the Coffee Management driver program

# This is the module used to delete coffee records

import os # Needed for remove and rename functions

def delete_coffee():
    # Create bool var
    found = False
    
    # Get coffee to delete.
    search = input('Which coffee do you want to delete? ')
    
    # Open original coffee.txt file.
    coffee_file = open('coffee.txt', 'r')
    
    # Open temp file
    temp_file = open('temp.txt', 'w')
    
    # Read first record's description field
    descr = coffee_file.readline()
    
    # Read the rest of the file
    while descr != '':
        # Read the qty field
        qty = float(coffee_file.readline())
        
        # Strip the new line
        descr = descr.rstrip('\n')
        
        # IF this is not the record to delete, write it to temp file
        if descr != search:
            # Write record to temp file
            temp_file.write(descr + '\n')
            temp_file.write(str(qty) + '\n')
        else:
            # Set the found flag to True.
            found = True
        
        # Read the next descr
        descr = coffee_file.readline()
    
    # Close coffee file and temp file
    coffee_file.close()
    temp_file.close()
    
    # Delete the original coffee.txt file.
    os.remove('coffee.txt')
    
    # Rename the temporary file.
    os.rename('temp.txt', 'coffee.txt')
    
    # If search value not found, display a message
    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')
        