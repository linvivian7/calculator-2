"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Map between user input and calculator functions
function_mappings = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "square": square,
    "cube": cube,
    "pow": power,
    "mod": mod
}

# Perform calculations until the user types 'q'
while True:
    # Prompt user for input
    input_string = raw_input(">")

    # Tokenize input on spaces
    tokens = input_string.split(" ")
    func = tokens[0]

    try:
        if tokens[0] == "q":
            break

        # Calculate functions that have 1 arg
        elif len(tokens) == 2:
            print function_mappings[func](int(tokens[1]))

        # Calculate functions that have 2 args
        elif len(tokens) == 3:
            print function_mappings[func](int(tokens[1]), int(tokens[2]))

    except:
        print "That is an invalid input"
        continue
