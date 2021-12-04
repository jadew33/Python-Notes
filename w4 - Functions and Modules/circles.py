"""This is a module that works on circles.
It includes two functions that compute the circumference and area of a circle.

Author: Ting Hu
Date: 2020-09-23
"""

import math

        
def calculate_circumference(the_radius):
        """This function computes the circumference of a circle.
        It takes one parameter, the radius, and returns the circumference."""
        circumference = 2*math.pi*the_radius
        return circumference


def calculate_area(the_radius):
        """This function computes the area of a circle.
        It takes one parameter, the radius, and returns the area."""
        area = math.pi*the_radius**2
        return area


#  This is how we can test this module by running it directly from here
if __name__ == "__main__":  #  This module is run directly
        print("This 'circles' module is executed directly")
        print(calculate_circumference(10))
        print(calculate_area(5))










































        

