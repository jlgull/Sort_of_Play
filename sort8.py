#!/usr/bin/python3
# Original Author: Tracy Baker
# Modified by: Jonathan Heard
# Sort a group of items; integers, floating point or string.
#   Using a Tracy's bubble sort in a "cone" design.
# Program name: sort8.py
#

# Import all required modules

# Import sample from the random module.

from random import sample, randint, uniform

"""  random.sample(population, k)
        Return a k length list of unique elements chosen from the population sequence or set. 
        Used for random sampling without replacement.
"""

# Import system and name from the os module.
from os import system, name

""" name    - The name of the operating system dependent module imported. 
                The following names have currently been registered: 'posix', 'nt', 'java'.

    system  - Execute the command (a string) in a subshell. 
                This is implemented by calling the Standard C function system(), and has the same 
                limitations. Changes to sys.stdin, etc. are not reflected in the environment of the
                executed command. If command generates any output, it will be sent to the interpreter
                standard output stream. The C standard does not specify the meaning of the return value 
                of the C function, so the return value of the Python function is system-dependent.            

"""

# Import the time library to allow for the timing of the sorting process

from time import thread_time_ns

#
# Define all functions used in this program
#

def clear():
    # Found on this website: https://www.geeksforgeeks.org/clear-screen-python/
    # Define the clear function, which is agnostic to the operating system
    # being used. In PyCharm you have to sent "Emulate terminal in output console",
    # which is found under the "Edit run configuration" tab.

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Variable definition section
#
# start_time    - Start time, used to time the sort process
#

# List variables
#
# word_list     - collection of 3 letter groups
# selected_list - Randomly selected list of items to be sorted.
# temp_list     - Hold the selected_list prior to sorting, for comparison usage.

# Integer variables
#
# i, j, k       - Counters for the loop variables
# size_of_list  - Holds the number of random groups to select
# done          - Used to determine if data type selection is complete, 1 = completed, 0 = not completed.
# p             - Counter for the number of passes in the sort routine.

# Preset any required variables

word_list = []
selected_list = []
temp_list = []
done = 0
p = 0

# Preset required list variables

selected_list = []
temp_list = []

# Start of the Main program.

clear()

# Select data_type to be sorted and how many.

# Set the default data_type to "string".
while done == 0:
    data_type = 'string'

    user_input = input(f'\nThis program will sort 3 data types. Integers, Floating Point or Strings (3 letter groups).'
                   f'\n\tPlease enter a sample of the data to be sorted: ')

    try:
        user_input = int(user_input)
        data_type = 'integer'
    except:
        pass

    if data_type == 'string':
        try:
            user_input = float(user_input)
            data_type = 'floating point'
        except:
            pass

    if (input(f'\nThe data type entered was {data_type}. If you would like to change it, enter y: ')) != 'y':
        done = 1

size_of_list = int(input(f"\nHow many {data_type} values would you like? "))

# Generate the type and number of items to be sorted.

# Generate the Random Integer values

if data_type == 'integer':
    for i in range(size_of_list):
        selected_list.append(randint(1, 64000))

# Generate the Random Floating Point values

elif data_type == 'floating point':
    for i in range(size_of_list):
        selected_list.append(uniform(1, 64000))

# Generate the Random 3 letter String groups.

# This portion of the program generates a list of 3 letter groups
else:
    for i in range(26):
        for j in range(26):
            for k in range(26):
                word_list.append(chr(i + 97) + chr(j + 97) + chr(k + 97))

    selected_list = sample(word_list, size_of_list)

print(f'\n\n Your list will be made up of {data_type}s.')

# Main sort process

# Save the original list for later review.

temp_list = selected_list[:]

# Start the timer for the sort process
start_time = thread_time_ns()

# Sort Routine
num_entries = len(selected_list) - 1
while p < len(selected_list):
    print(f'\nPASS NUMBER {p + 1}')

    for i in range(num_entries):

        if selected_list[i] > selected_list[i + 1]:
            print(f'+++ swapping {selected_list[i]} with {selected_list[i + 1]}')
            temp = selected_list[i]
            selected_list[i] = selected_list[i + 1]
            selected_list[i + 1] = temp
        else:
            print(f'--- NOT swapping {selected_list[i]} with {selected_list[i + 1]}')

        print(f'The current list: {selected_list}\n')

    num_entries -= 1
    p += 1

# Print out the results

print(f'\nThe list to be sorted had {len(selected_list)} items in it.')
print(f'The original, unsorted, list:\n\t{temp_list}')

print(f'\nThe sorted list (after {p} passes):\n\t{selected_list}')
print(f"\n\t\t---  {(thread_time_ns() - start_time)/1e3:,.0f} microseconds  ---" )
