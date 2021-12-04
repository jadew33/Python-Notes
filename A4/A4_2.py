"""
This program uses recursion to return a list of possible paths, hopping
1 or 2 squares at a time.

Jade Wei (20224398)
February 2, 2021
"""


def find_paths(path, start, n):
    # Recursive function to find all possible paths, hopping 1 or 2 squares
    hopping_paths = []

    if start == n:  # Base case
        return [path]

    if start + 1 <= n:  # To check if jumping by 1 is valid and reset start
        hopping_paths.extend(find_paths(path + '-' + str(start + 1),
                                        start + 1, n))

    if start + 2 <= n:  # To check if jumping by 2 is valid and reset start
        hopping_paths.extend(find_paths(path + '-' + str(start + 2),
                                        start + 2, n))

    return hopping_paths


def hopping_game(n):
    """Passes number of squares, n, to a second function with extra parameters
    to return a list of all possible hopping paths"""
    hopping_paths = find_paths('0', 0, n)  # Paths all begin with 0
    return hopping_paths


if __name__ == "__main__":
    print(hopping_game(1))
    print(hopping_game(2))
    print(hopping_game(3))
    print(hopping_game(4))
