# How to use this library
# First you have to put the folder in the same folder of your script
# Then you'll have to import the folder and the file
# $ from CalcLib import calculator
# Then if you want to use functions inside you just have to use them like this
# calculator.addition(x1, x2) | calculator.subtraction(y1, y2) and so on.
# The functions will return the result so you have to print() it.
# I will provide a test file with the script.


def addition(x1, x2):
    result = x1 + x2
    return "The addition result is: " + str(result)

def subtraction(x1, x2):
    result = x1 - x2
    return "The subtraction result is: " + str(result)

def multiplication(x1, x2):
    result = x1 * x2
    return "The multiplication result is: " + str(result)

def division(x1, x2):
    result = x1 / x2
    return "The division result is: " + str(result)
