"""This program helps FunSplash estimate costs for pool covers and fencing
by computing the area or circumference of a circle with a given radius.

This version moves the output to the main function.

Author: Ting Hu
Date: 2020-09-22
"""

import math


def get_input():
        """This function gets the radius and task from the user. It has no
        parameters and returns the radius as a float and the task as a
        string."""
        next_radius = float(input("Enter the value of the radius of the pool:"))
        print("\nEnter your choice of task.")
        next_task = input("C to compute circumference, "\
                         "A to compute area: ")
        return next_radius, next_task
        

def calculate_circumference(the_radius):
        """This function computes the circumference of a circle. It inputs the
        radius and returns the circumference."""
        circumference = 2*math.pi*the_radius
        return circumference


def calculate_area(the_radius):
        """This function computes the area of a circle. It inputs the radius and
        returns the area."""
        area = math.pi*the_radius**2
        return area


def main():
        """This function is the main execution."""
        radius, task_to_do = get_input()

        if (task_to_do =="C") or (task_to_do =="c"):  # Compute circumference
                circumference = calculate_circumference(radius)
                print("The circumference of a pool of radius",radius,\
                              "is","%6.3f"%circumference)
        else:  # Compute area
                area = calculate_area(radius)
                print("The area of a pool of radius",radius,\
                              "is","%6.3f"%area)


# Program starts here
main()























