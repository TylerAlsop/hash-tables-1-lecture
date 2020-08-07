# Print out all of the strings in the following array in alphabetical order, each on a separate line.
# ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']
# The expected output is:
# 'Cha Cha'
# 'Foxtrot'
# 'Jive'
# 'Paso Doble'
# 'Rumba'
# 'Samba'
# 'Tango'
# 'Viennese Waltz'
# 'Waltz'
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.



###################### My Code ######################

# U.
# We're given an array. We need to sort the array alphabetically and then print out each of the items in the array. Each item should be on it's own line.

# P.
# 1. Set the array to a variable name.
# 2. Sort the array.
# 3. Create a function that Loops over the array.
#     a. Return a print function that prints each item on its own line.

# E.

dances = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']

def print_each_dance (array):
    array.sort()
    for item in array:
        print(item)

print_each_dance(dances)

# R. REVISED PLAN
# 1. Set the array to a variable name.
# 2. Create a function
#   a. Function will:
        # 1. Take in an array as an argument.
        # 2. Sort the array.
        # 3. Loop over the sorted array with a for loop.
        #     a. Loop will print each item in the array.
# 3. Call the function and pass in the array.