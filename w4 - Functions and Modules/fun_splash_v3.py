"""This program helps FunSplash estimate costs for pool covers and fencing
by computing the area or circumference of a circle with a given radius.

This version gets rid of all global variables.

Author: Ting Hu
Date: 2020-09-22
"""

import math


def get_input():
        """This function getst input from the user"""
        next_radius = float(input("Enter the value of the radius of the pool:"))
        print("\nEnter your choice of task.")
        next_task = input("C to compute circumference, A to compute area: ")
        return next_radius, next_task

        
def calculate_circumference(the_radius):
        """This function computes the circumference of a circle"""
        circumference = 2*math.pi*the_radius
        print("The circumference for a pool of radius",\
              the_radius, "is", "%6.3f"%circumference)


def calculate_area(the_radius):
        """This function computes the area of a circle"""
        area = math.pi*the_radius**2
        print("The area for a pool of radius",\
              the_radius, "is", "%6.3f"%area)


def main():
        radius, task_to_do = get_input()

        if (task_to_do =="C") or (task_to_do =="c"):  # Compute circumference
                calculate_circumference(radius)
        else: # Compute area
                calculate_area(radius)


# Program starts here
main()


