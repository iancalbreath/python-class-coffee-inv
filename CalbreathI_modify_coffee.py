# Mac Littlefield's class
# Ian Calbreath
# Creating modules for the Coffee Management driver program

# This is the module used to modify coffee records

import os  # Needed for remove and rename functions

def modify_coffee():
    # Create a bool variable to use as a flag.
    found = False
    
    # Get the search value and the new quantity.
    search = input('Enter a description to search for: ')
    new_qty = float(input('Enter the new quantity: '))
    
    # Open the original coffee.txt file.
    coffee_file = open('coffee.txt', 'r')
    
    # Open the temp file
    temp_file = open('temp.txt', 'w')
    
    # Read the first record's descr field.
    descr = coffee_file.readline()
    
    # Read the rest of the file.
    while descr != '':
        # Read the qty field.
        qty = float(coffee_file.readline())
        
        # Strip the \n from the descr
        descr = descr.rstrip('\n')
        
        # Write either this record to the temp file, or the new record if this is the one that is to be modified
        if descr == search:
            # Write the modified record to the temp file.
            temp_file.write(descr + '\n')
            temp_file.write(str(new_qty) + '\n')
            
            # Set the found flag to True
            found = True
        else:
            # Write the original record to the temp file.
            temp_file.write(descr + '\n')
            temp_file.write(str(qty) + '\n')
            
        # Read the next descr
        descr = coffee_file.readline()
       
    # Close the coffee file and the temp file
    coffee_file.close()
    temp_file.close()
    
    # Delete original coffee.txt file.
    os.remove('coffee.txt')
    
    # Rename the temporary file.
    os.rename('temp.txt', 'coffee.txt')
    
    # If the search value was not found in the file display a message
    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')
        