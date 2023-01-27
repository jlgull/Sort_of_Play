#!/usr/bin/python3
# Original Author: Tracy Baker
# Modified by: Jonathan Heard
# Sort a group of items; integers, floating point or string.
#   Using a bubble sort in a "cone" design.
# Program name: sort7a.py
#

# Variable definition section
#
# start_time    - Start time, used to time the sort process
#

# Import all required libraries.

# Import the time library to allow for the timing of the sorting process
#

import time

# Preset required list variables

user_list = []
temp_list = []
i = 1
j = 0
data_type = 'string'

user_input = input(f'\n\nPlease enter item #{i} for the list to be sorted: ')
i += 1

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

if data_type != 'string':
    if (input(f'The data type is {data_type}. Would you like it to be a string (y for yes): ')) == 'y':
        data_type = 'string'

user_list.append(user_input)

print(f'\n\n Your list will be made up of {data_type}s.')

while True:
    user_input = input(f'\nWhat\'s the #{i} {data_type} item in the list (Enter to quit): ')

    if user_input == '':
        break

    if data_type == 'integer':
        try:
            user_input = int(user_input) 
        except:
            print('\nPlease enter an integer (whole number).')
            continue

    elif data_type == 'floating point':
        try:
            user_input = float(user_input)
        except:
            print('\nPlease enter a floating point number.')
            continue
            
    user_list.append(user_input)
    i += 1


# Main sort process

# Start the timer

start_time = time.thread_time_ns()

# Sort Routine
num_entries = len(user_list) - 1
while j < len(user_list):
    print(f'\nPASS NUMBER {j + 1}')

    for i in range(num_entries):

        if user_list[i] > user_list[i + 1]:
            print(f'+++ swapping {user_list[i]} with {user_list[i + 1]}')
            temp = user_list[i]
            user_list[i] = user_list[i + 1]
            user_list[i + 1] = temp
            temp_list = user_list
        else:
            print(f'--- NOT swapping {user_list[i]} with {user_list[i + 1]}')
            if user_list == temp_list and i == num_entries :
                # j = len(user_list) + 1

        print(f'The current list: {user_list}\n')

    num_entries -= 1
    j += 1

print(f'\nThe list has {len(user_list)} items in it.')
print(f'The original, unsorted, list: {user_list}')

print(f'\nThe sorted list ({j} passes): {user_list}')
print(f"--- {time.thread_time_ns() - start_time:,.0f} nanoseconds ---" )
