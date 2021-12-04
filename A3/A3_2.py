"""This program first uses list_generator to generate 3 randomized lists,
one ascending, one descending, and one randomized.
Then, this program uses quadratic_sorts to sort these lists and records the
amount of inner loops, outer loops, and swaps each type of sorting requires.

Jade Wei (20224398)
January 31, 2021
"""

import list_generator
import quadratic_sorts


def print_statements(case, counter, new_sort, sort_type):
    # To simplify output

    if new_sort:  # for each new type of sort
        print()
        print(sort_type)
        print("               ", "# outer loops", "# inner loops", "# swaps",
              sep="\t")

    print(case, str(counter[0]), str(counter[1]), str(counter[2]),
          sep="\t\t\t")


def main():
    a_length = int(input("Please enter the length of input lists: "))

    best_case = list_generator.list_ascending(a_length)

    worst_case = list_generator.list_descending(a_length)
    worst_case2 = list(worst_case)
    worst_case3 = list(worst_case)

    random_case = list_generator.list_randomized(a_length)
    random_case2 = list(random_case)
    random_case3 = list(random_case)

    print("Best-case example: " + str(best_case))
    print("Worst-case example: " + str(worst_case))
    print("Randomized example: " + str(random_case))

    # Insertion sort:
    print_statements("Best-case      ",
                     quadratic_sorts.insertion_sort(best_case), True,
                     "Insertion sort:")
    print_statements("Worst-case     ",
                     quadratic_sorts.insertion_sort(worst_case),
                     False, "")
    print_statements("Randomized-case",
                     quadratic_sorts.insertion_sort(random_case),
                     False, "")

    # Selection sort:
    print_statements("Best-case      ",
                     quadratic_sorts.selection_sort(best_case),
                     True, "Selection sort:")
    print_statements("Worst-case     ",
                     quadratic_sorts.selection_sort(worst_case2),
                     False, "")
    print_statements("Randomized-case",
                     quadratic_sorts.selection_sort(random_case2),
                     False, "")

    # Bubble sort:
    print_statements("Best-case      ", quadratic_sorts.bubble_sort(best_case),
                     True, "Bubble sort:")
    print_statements("Worst-case     ",
                     quadratic_sorts.bubble_sort(worst_case3),
                     False, "")
    print_statements("Randomized-case",
                     quadratic_sorts.bubble_sort(random_case3),
                     False, "")


main()
