"""This program helps the company FunSplash
estimate costs for pool covers and fencing
by computing the area or circumference of a circle with a given radius.

Author: Ting Hu
Date: 2020-09-22
"""


import math   # Use Python module math to get the value of PI


radius = float(input("Enter the value of the radius of the pool: "))

print("\nEnter your choice of task.")
task_to_do = input("C to compute circumference, A to compute area: ")

if (task_to_do == "C") or (task_to_do == "c"):
    circumference = 2*math.pi*radius
    print("\nThe circumference for a pool of radius", radius, \
          "is", "%6.3f"%circumference)       
else:
    area = math.pi*radius*radius
    print("\nThe area for a pool of radius", radius, \
          "is", "%6.3f"%area)

