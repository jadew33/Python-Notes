"""
Jade Wei (20224398)
October 14, 2020
CISC 121 - Assignment 2 module

Contains 3 functions:
cal_factorial(x):
    receives a positive integer “x” and returns the factorial of that number.
list_multiples(number, length):
    takes a non-negative integer “number” and a positive integer “length”,
    and returns a list of multiples of “number” up to “length”.
find_max(a_list):
    takes a list of integers and returns the maximum number.
"""


def cal_factorial(x):
    #  Receives a positive int x and returns the factorial using recursion

    # Catches empty, neg, or 0 inputs
    if x == "" or x < 0:
        return "Must be a positive int"
    if x == 0:
        return 1

    # To calculate factorial
    if x == 1:
        return x
    else:
        return x * cal_factorial(x - 1)


def list_multiples(number, length):
    #  Takes positive ints "number" and "length and returns a list of multiples of "number" up to "length"

    # Handles empty, neg, or 0 inputs
    if number == "" or length == "" or number < 0 or length < 0:
        return "Must be positive integers"
    if number == 0:
        return 0

    multiples = []
    for i in range(1, length + 1):
        multiples.append(number * i)
    return multiples


def find_max(a_list):
    #  Takes a list of integers and returns the maximum number

    if a_list == "":
        return "Must enter a list of integers"
    if isinstance(a_list, int):
        return a_list

    largest = -999
    for i in range(0, len(a_list)):
        if largest < a_list[i]:
            largest = a_list[i]
    return largest


if __name__ == "__main__":
    # cal_factorial()
    # Case 1 - Empty input
    print(cal_factorial(""))
    # Case 2 - 1
    print(cal_factorial(1))
    # Case 3 - 0
    print(cal_factorial(0))
    # Case 4 - Any number
    print(cal_factorial(15))
    # Case 5 - Neg number
    print(cal_factorial(-15))
    print()

    # list_multiples()
    # Case 1 - 0
    print(list_multiples(0, 5))
    # Case 2 - 1
    print(list_multiples(1, 4))
    # Case 3 - Any number
    print(list_multiples(4, 6))
    # Case 4 - Neg number
    print(list_multiples(-1, -1))
    # Case 5 - Empty input
    print(list_multiples("", ""))
    print()

    # find_max()
    # Case 1 - Empty input
    print(find_max(""))
    # Case 2 - 1 number
    print(find_max(10))
    # Case 3 - Max is last number
    print(find_max([1, 3, 5]))
    # Case 4 - Max is first number
    print(find_max([5, 2, 1]))
    # Case 5 - Max is middle number
    print(find_max([1, 5, 80, 4]))
    # Case 6 - 0 is in the list
    print(find_max([0, 4]))
    # Case 7 - Neg number list
    print(find_max([-5, -6, -9]))
