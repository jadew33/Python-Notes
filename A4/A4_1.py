"""This program uses a recursive binary search algorithm to locate first
occurrence of b in a string of only a and b

Jade Wei (20224398)
February 2, 2021
"""


def find_first_b(a_string, start):
    # This function either returns the index of the first b or None

    end = len(a_string) - 1

    # To handle case where string begins with b
    if a_string[0] == 'b':
        return 0

    # Uses recursion / base case to replace while loop in binary search
    if start <= end:

        # Find middle index, taking recursion loops into account
        mid = start + (end - start) // 2

        # To compensate if the index overshoots and misses the first b
        if a_string[mid] == 'b' and a_string[mid - 1] == 'b':
            return mid - 1

        elif a_string[mid] == 'b':
            return mid

        # b will always be to the right of a, so search right half
        elif a_string[mid] == 'a':
            return find_first_b(a_string, mid + 1)

    # If there is no b in the string
    else:
        return None


if __name__ == "__main__":
    print(find_first_b("aabbb", 0))  # b at index 2
    print(find_first_b("aaaabbbb", 0))  # b in the middle of string
    print(find_first_b("aaaaaaaaa", 0))  # no b
    print(find_first_b("bbb", 0))  # b at beginning
    print(find_first_b("aaaaaab", 0))  # b at index 6
