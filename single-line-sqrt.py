#!/usr/bin/python3
#
# Author: Jonathan Heard
# Create a single line square root print of any value.
# Program name: single-line-sqrt.py

# Import all required modules

# Import sqrt and fabs from the math module.

from math import sqrt, fabs


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


# Integer variables


# Preset any required variables

do_again = ""
word_list = []
selected_list = []

# Clear the screen, prior to the program.
clear()

# Main body of the program.

# This portion request the number to calculate the square root from.

while do_again != "N":

    # Clear the screen, prior to the program.
    clear()

    print(f"\nThis program will accept any signed number, either integer or floating point, and "
          "\nprint the absolute value of the signed number and then the square root signed number."
          "\nThis will include the 'i' for negative values.")


    try:
        # Input to gather a numeric value, can be positive or negative.

        base_number_1 = input(f"\nEnter a number, it can be positive or negative: ")
        base_number = float(base_number_1)
    except ValueError:
        print(f"The entry, {base_number_1}, was not a number, please try again.")
        continue

    print(f"\n\tThe floating point number entered was:\t\t{base_number:.3f}"
        f"\n\tThe absolute value of the entered number is:\t{fabs(base_number):.3f}"
        f"\n\tThe square root of the entered number is:\t"
        f"{sqrt(base_number) if base_number > 0 else str(sqrt(fabs(base_number))) + ' i'}")

    # Ask if the user would like to play again.
    # Also, validate for the correct response.
    while True:
        do_again = input("\nWould you like to play again? Enter (Y) for yes or (N) for no. ").upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or a N.")

# End of Program