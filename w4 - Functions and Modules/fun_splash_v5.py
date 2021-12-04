"""This program helps FunSplash estimate costs for pool covers and fencing
by computing the area or circumference of a circle with a given radius.

This version uses our module cicles.

Author: Ting Hu
Date: 2020-09-23
"""

import circles


def get_input():
        """This function getst input from the user"""
        next_radius = float(input("Enter the value of the radius of the pool:"))
        print("\nEnter your choice of task.")
        next_task = input("C to compute circumference, "\
                         "A to compute area: ")
        return next_radius, next_task

        
def main():
        radius, task_to_do = get_input()

        if (task_to_do =="C") or (task_to_do =="c"):  # Compute circumference
                circumference = circles.calculate_circumference(radius)
                print("The circumference of a pool of radius",radius,\
                      "is","%6.3f"%circumference)
        else:  # Compute area
                area = circles.calculate_area(radius)
                print("The area of a pool of radius",radius,\
                      "is","%6.3f"%area)


# Program starts here
main()

