"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic1 import *


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


def my_reduce(func, iterables):
    """Apply function of two arguments cumulatively to iterables

    args:
        func: any user-defined function
        iterables: any iterable data type
    returns:
        result
    """

    first = iterables[0]
    second = iterables[1]

    result = func(first, second)

    for new_num in iterables[2:]:
        result = func(result, new_num)
    return result


def compute(math_operator, numbers):
    """Calculate function with variable args.

    args:
        math_operator: add, subtract, multiply, divide,
            square, cube, power, and mod (see arithmetic1.py)
        numbers: a list of numbers to iterate over
    returns:
        The computed math function on the numeric list
    """
    return my_reduce(lambda x, y: math_operator(int(x), int(y)), numbers)


# Perform calculations until the user types 'q'
while True:
    # Prompt user for input
    input_string = raw_input(">").rstrip()

    # Tokenize input on spaces
    tokens = input_string.split(" ")
    func = tokens[0]

    # Quit program
    if tokens[0] == "q":
        break
    # Give error if operator is not defined
    elif func not in function_mappings:
        print "Please input a valid operator"
        continue

    # Print out error messages for incorrect number of operands
    if func in ["+", "-", "*", "/"]:
        if len(tokens) < 3:
            print "Please enter at least 2 operands"
            continue
    elif func in ["square", "cube"]:
        if len(tokens) > 2:
            print "Please only input 1 operand"
            continue
    elif func in ["pow", "mod"]:
        if len(tokens) != 3:
            print "Please enter only 2 operands"
            continue

    try:
        # Run compute function starting at index 1
        result = compute(function_mappings[func], tokens[1:])
        print "Result = {:.2f}".format(result)

    # Expect TypeError when non-integers are entered after index 1
    # Expect ValueError when math operation cannot be completed (i.e. dividing by 0)
    except TypeError, ValueError:
        print "That is an invalid input"
