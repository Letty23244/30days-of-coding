# AKA DATA COLLECTIONS

#lists
#sets
#Dictionaries
# Tuples 

#1. LISTS(CRUD)

# They store multiple items
# CRUD =(Create, Read, Update, Delete)
#Syntax
    # They use square brackets
    # The variables items have to be of the same type.
    # They are mutable
    # They work with index
    
studnet_name =['Sandra', 'Patrica', 'Phiona', 'Anitah'] # strings
student_marks = [80, 56, 75, 60] # integers
data = ['Favour', 99, 'Kamwokya']

#Access the whole list
print(studnet_name, type(studnet_name))

# Acessing list items
# INDEX are used 
# Positive indexing(Starts from the left)
print(studnet_name[0]) # first item
print(studnet_name[1]) # second item
print(studnet_name[2]) # third item
print(studnet_name[3]) # last item

# Negative indexing(starts from the right)
print(studnet_name[-4]) # first item
print(studnet_name[-3]) # second item
print(studnet_name[-2]) # third item
print(studnet_name[-1]) # last item

# Appending an item
# Adding new items at the end of the list
studnet_name.append('Micheal')
print(studnet_name)

# Inserting an item
# Adds the items in any position using an index
studnet_name.insert(2, 'Faith')
print(studnet_name)



# Assignment 

# Print Paritca Phiona and Anitah.
# Add Masha at the fourth position.
# Update the name Phionah to Phionah Aladinnah.
# Display the length of the students list
# Print all the students names having updated the list using a for loop
# Calculate the total marks for the students marks variables
