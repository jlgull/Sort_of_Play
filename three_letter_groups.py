#!/usr/bin/python3
#
# Author: Jonathan Heard
# Create a collection of 3 letter groups.
# Program name: three_letter_groups.py

# Import all required modules

# Import sample from the random module.
from random import sample

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

#
# Define the clear function definition for use in this program
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


# List of all the Variables used in this module/program

# List variables

# word_list     - collection of 3 letter groups
# selected_list - randomly selected short list of groups

# Integer variables

# i, j, k       - counters for the loop variables
# size_of_list  - Holds the number of random groups to select

# Preset any required variables

word_list = []
selected_list = []

# Clear the screen, prior to the program.
clear()

# Main body of the program.

# This portion of the program generates a list of 3 letter groups

for i in range(26):
    for j in range(26):
        for k in range(26):
            word_list.append(chr(i + 97) + chr(j + 97) + chr(k + 97))

# Once built, the program asks how many you would like in a shorter list.

size_of_list = int(input(f"\nThis program has generated {len(word_list)} 3 letter groups.\n\tHow many would you like? "))

# Randomly select the desired number and create the selected_list.
selected_list = sample(word_list, size_of_list)

# Print the results of the program.
print(f"\nHere are the {size_of_list} randomly chosen groups from the {len(word_list)} possible groups."
      f"\n\n {selected_list}" )
