"""
Jade Wei (20224398)
October 14, 2020
CISC 121 - Assignment 2 module

Executes the 3 functions in fun_math module using user input
"""
import fun_math


def main():
    choice = input("Please choose your task:\n"
                   "1 - Calculate Factorial\n"
                   "2 - Generate a list of multiples\n"
                   "3 - Find max number in a list\n")

    while choice != 1 and choice != 2 and choice != 3 and choice != 0:

        # cal_factorial()
        if choice == "1":
            x = input("Please enter a non-negative integer: ")
            while x == "" or not x.isnumeric() or x.isspace() or int(x) < 0:
                x = input("Please enter a non-negative integer: ")
            print("The factorial of " + str(x) + " is " + str(fun_math.cal_factorial(int(x))))
            choice = "ask_input"

        # list_multiples()
        elif choice == "2":

            # Asks for user inputs while checking for invalid input
            number = input("Please enter a non-negative integer: ")
            while number == "" or not number.isnumeric() or number.isspace() or int(number) < 0:
                number = input("Please enter a non-negative integer: ")
            length = input("Please enter how many multiples: ")
            while length == "" or not length.isnumeric() or length.isspace() or int(length) < 0:
                length = input("Please enter a non-negative integer: ")

            print(str(length) + " multiples of " + str(number) + " is: ", end='')
            print(fun_math.list_multiples(int(number), int(length)))
            choice = "ask_input"

        # find_max()
        elif choice == "3":
            list = []

            print("For a negative number, type 'neg', otherwise ", end='')
            x = input("please input numbers, one at a time: ").lower()

            while x != "stop":

                # To accept neg input
                if x == "neg":
                    x = int(input("Please enter the absolute value of the number: "))
                    x = -x

                # Handles empty, spaces, or non-numeric input
                else:
                    while x == "" or x.isspace() or not x.isnumeric():
                        x = input("Please input a valid number: ").lower()

                list.append(int(x))
                x = input("Please input another number or type 'stop' to end list: ").lower()

            print("The max of ", end='')
            print(list, end='')
            print(" was ", end='')
            print(fun_math.find_max(list))
            choice = "ask_input"

        # Continues prompting user if no valid response is given
        else:
            choice = input("Invalid response.\n"
                           "Please choose your task:\n"
                           "1 - Calculate Factorial\n"
                           "2 - Generate a list of multiples\n"
                           "3 - Find max number in a list\n")

        # Prompt to ask user if they would like to select another option
        if choice == "ask_input":
            choice = input("\nPlease choose another task or enter 0 to exit:\n"
                           "1 - Calculate Factorial\n"
                           "2 - Generate a list of multiples\n"
                           "3 - Find max number in a list\n")

        if choice == "0":
            exit()


main()
