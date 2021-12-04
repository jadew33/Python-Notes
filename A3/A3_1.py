"""This program uses binary search to find the integer value the user had in
mind.

Jade Wei (20224398)
January 28, 2021
"""


def binary_search(lower, upper):
    """This function uses binary search to guess the user's number."""

    while int(lower) <= int(upper):

        mid = (int(lower) + int(upper)) // 2
        response = input("Is the number greater than " + str(mid) + " (y/n)? ")

        if response == ('n' or 'N'):
            upper = mid - 1
        elif response == ('y' or 'Y'):
            lower = mid + 1
        else:  # To ensure valid user input
            print("Please respond with (y/n)")

    if response == 'y':
        """ To compensate for result ending up being 1 too small if the 
        algorithm had already guessed correctly as upper then becomes 
        (guess - 1), excluding the guess from range"""
        return mid + 1
    else:
        return mid


def main():
    lower = input("Please enter the lower bound: ")
    upper = input("Please enter the upper bound: ")
    print("Your number is: " + str(binary_search(lower, upper)))


main()
