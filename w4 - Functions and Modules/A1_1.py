"""
Jade Wei (20224398)
Sept 27 2020
CISC 121 - Assignment 1_1

A1_1: Input and output, strings, while loop
Write a Python program that asks the user to enter their first name and prints it in all capital letters.
If the input is “John”, the program should print “Your name in all capital letters is JOHN.”
If the input is “amy”, the program should print “Your name in all capital letters is AMY.”
If the input is “123”, the program should print “Please try again and enter your name.”
If the input is “ ” , the program should print “Please try again and enter your name.”
Once this is done, ask the user if they would like to do it again. If yes, prompt the message to enter their name again;
otherwise, exit the program.
 """

# initial name prompt
name = input("Please enter your first name: ")

while name != "exit":
    # Checks if name entered is not numeric and doesn't contain spaces (as this program is just first names)
    if not name.isalpha():
        # Asks for name again for errors. The lower() is there in case the user inputs "exit" to exit
        name = input("Please try again and enter your name using only valid characters. ").lower()
    else:
        # Converts name entered to uppercase and prompts user to repeat or exit
        print("Your name in all capital letters is " + name.upper())
        name = input("Please enter your name again if you would like to do it again, or input 'exit'. ").lower()
print("Thank you and goodbye")
