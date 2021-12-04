"""This program helps FunSplash estimate costs for pool covers and fencing
by computing the area or circumference of a circle with a given radius.

This version demonstrates different scopes of variables, local or global.

Note: This program DOES NOT WORK!!

Author: Ting Hu
Date: 2020-09-22
"""

import math


def get_input():
        """This function gets the input from user"""
        radius = float(input("Enter the value of the radius of the pool:"))
        print("\nEnter your choice of task.")
        task_to_do = input("C to compute circumference, A to compute area: ")

        
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

# Create global variables radius and taskToDo and initialize their values
radius = 0      
task_to_do = "A"      
        
get_input()

if (task_to_do =="C") or (task_to_do =="c"):  # compute circumference
        calculate_circumference()
else:   # compute area
        calculate_area()
