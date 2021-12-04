"""This module provides two functions that operate on lists.
Function merge_two combines two lists.
Function remove_duplicates removes duplicate elements in a list.

Author: Ting Hu
Date: 2020-09-29
"""

def merge_two(list_1, list_2):
    """This function merges two lists."""
    total = list(list_1)
    for item in list_2:
        total.append(item)
    return total
    

def remove_duplicates(a_list):
    """This function removes duplicates in a list and returns a new list."""
    copy = []
    for item in a_list:
        if item not in copy:
            copy.append(item)
    return copy


if __name__ == "__main__":
    # Module testing

    # function merge_two

    # Case 1
    a_list = []
    b_list = ["brandX","brandY"]
    print("The input lists are", a_list, b_list)
    m_list = merge_two(a_list, b_list)
    print("The merged list is", m_list)
    print("\n")

    # Case 2
    a_list = ["brandX","brandY"]
    b_list = ["brandX","brandY"]
    print("The input lists are", a_list, b_list)
    m_list = merge_two(a_list, b_list)
    print("The merged list is", m_list)
    print("\n")

    # Case 3
    a_list = ["brandX","brandY"]
    b_list = ["brandX"]
    print("The input lists are", a_list, b_list)
    m_list = merge_two(a_list, b_list)
    print("The merged list is", m_list)
    print("\n")

    # Case 4
    a_list = ["brandX","brandY"]
    b_list = ["brandX","brandY","brandZ"]
    print("The input lists are", a_list, b_list)
    m_list = merge_two(a_list, b_list)
    print("The merged list is", m_list)
    print("\n")

    # Case 5
    a_list = ["brandY"]
    b_list = ["brandX","brandZ"]
    print("The input lists are", a_list, b_list)
    m_list = merge_two(a_list, b_list)
    print("The merged list is", m_list)
    print("\n")
    
    # function remove_duplicates

    # Case 1
    a_list = []
    print("The input list is",a_list)
    a_unique = remove_duplicates(a_list)
    print("After calling remove_duples:", a_unique)
    print("\n")

    # Case 2
    a_list = ["brandX","brandY"]
    print("The input list is",a_list)
    a_unique = remove_duplicates(a_list)
    print("After calling remove_duples:", a_unique)
    print("\n")

    # Case 3
    a_list = ["brandX","brandY","brandX"]
    print("The input list is",a_list)
    a_unique = remove_duplicates(a_list)
    print("After calling remove_duples:", a_unique)
    print("\n")
    
    # Case 4
    a_list = ["brandX","brandX","brandY","brandX","brandZ",]
    print("The input list is",a_list)
    a_unique = remove_duplicates(a_list)
    print("After calling remove_duples:", a_unique)
    print("\n")

    # Case 5
    a_list = ["brandZ","brandZ","brandZ","brandZ"]
    print("The input list is",a_list)
    a_unique = remove_duplicates(a_list)
    print("After calling remove_duples:", a_unique)
    print("\n")







    
