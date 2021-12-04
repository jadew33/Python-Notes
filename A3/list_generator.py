"""This module contains three functions which generate a random list in
ascending, descending, and randomized orders.

Jade Wei (20224398)
January 31, 2021
"""
import random


def list_ascending(a_length):
    a_list = [round(random.uniform(0, 100), 2) for i in range(a_length)]
    a_list.sort()
    return a_list


def list_descending(a_length):
    a_list = [round(random.uniform(0, 100), 2) for i in range(a_length)]
    a_list.sort(reverse=True)
    return a_list


def list_randomized(a_length):
    a_list = [round(random.uniform(0, 100), 2) for i in range(a_length)]
    return a_list
