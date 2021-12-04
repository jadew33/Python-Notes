"""This module contains three functions that perform insertion sort,
selection sort, and bubble sort on a list, all coded using course notes.

Jade Wei (20224398)
January 31, 2021
"""


def insertion_sort(a_list):
    counter = [0, 0, 0]  # [outer loops, inner loops, swaps]
    for key in range(1, len(a_list)):
        counter[0] += 1  # number of outer loops
        i = key
        while i > 0 and a_list[i - 1] > a_list[i]:
            counter[1] += 1  # number of inner loops
            counter[2] += 1  # number of swaps
            a_list[i - 1], a_list[i] = a_list[i], a_list[i - 1]
            i = i - 1
    return counter


def selection_sort(a_list):
    counter = [0, 0, 0]  # [outer loops, inner loops, swaps]
    n = len(a_list)
    for i in range(n - 1):
        current_min = i
        counter[0] += 1  # number of outer loops
        for j in range(i + 1, n):
            counter[1] += 1  # number of inner loops
            if a_list[j] < a_list[current_min]:
                current_min = j
        if current_min != i:
            counter[2] += 1  # number of swaps
            a_list[i], a_list[current_min] = a_list[current_min], a_list[i]
    return counter


def bubble_sort(a_list):
    counter = [0, 0, 0]  # [outer loops, inner loops, swaps]
    swap_flag = True
    n = len(a_list)
    while swap_flag:
        swap_flag = False
        counter[0] += 1  # number of outer loops
        for i in range(1, n):
            counter[1] += 1  # number of inner loops
            if a_list[i - 1] > a_list[i]:
                counter[2] += 1  # number of swaps
                a_list[i - 1], a_list[i] = a_list[i], a_list[i - 1]
                swap_flag = True
        # n -= 1 #  Improved bubble sort cuts the worst-case inner loops to 10
    return counter
