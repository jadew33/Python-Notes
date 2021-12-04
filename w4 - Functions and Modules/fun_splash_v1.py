"""This program helps FunSplash estimate costs for pool covers and fencing
by computing the area or circumference of a circle with a given radius.

This version defines two functions for the computations
of circumference and area of a circle.

Author: Ting Hu
Data: 2020-09-22
"""

import math


def calculate_circumference():
        """This function computes the circumference of a circle"""
        circumference = 2*math.pi*radius
        print("\nThe circumference for a pool of radius", radius, \
              "is", "%6.3f"%circumference)


def calculate_area():
        """This function computes the area of a circle"""
        area = math.pi*radius**2
        print("\nThe area for a pool of radius", radius, \
              "is", "%6.3f"%area)



# Main section of the program
radius = float(input("Enter the value of the radius of the pool:"))

# Ask the choice of task
print("\nEnter your choice of task.")
task_to_do = input("C to compute circumference, A to compute area: ")

if (task_to_do =="C") or (task_to_do =="c"):  # Compute circumference
        calculate_circumference()
else:  # Compute area
        calculate_area()

