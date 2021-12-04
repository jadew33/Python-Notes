"""This program illustrate data flow in Python functions
There are four types, none, only_in, only_out, and in_out.

Author: Ting Hu
Date: 2020-09-25
"""

def question():
      """ This function needs no data and returns no data."""
      print("How does data flow in and out of functions?")


def only_in(x):
      """ This function receives data but does not return any data."""
      print("The value of x is ", x)


def only_out():
      """ This function needs no data but creates and returns a value."""
      new_value = 5
      return new_value


def in_out(x):
      """ This function receives a value, modifies it, and returns it."""
      x = x+5
      return x


def main():
      question()
      only_in(10)
      y = only_out()
      print(y)
      z = in_out(y)
      print(z)


main()
      
