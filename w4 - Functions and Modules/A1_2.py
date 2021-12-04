"""
Jade Wei (20224398)
Sept 27 2020
CISC 121 - Assignment 1_2

1_2: Two-dimensional lists, dictionary, file I/O
Write a Python program that utilizes friendship network data (see in attachment) and computes the number of friends
for each person.
In the input file friendship.txt, each line shows the names of two persons who are friends with each other
Note that each pair will only be represented once in the file. So “Michael    Anna” and “Anna    Michael”
represent the same friendship and will not both appear in the file.
The program outputs the number of friends Michael, Anna, Amy, and Max each has as follows (in any order):
Michael has 2 friends.
Anna has 3 friends.
Amy has 1 friend.
Max has 2 friends.
Hint: Use a two-dimensional list, i.e., a list of lists, to store the friendship network.
You may also consider using a dictionary.
 """

network = {}  # Stores friendship network
friends = []  # Stores lines in file

# To read file
try:
    friend_file = open("friendship.txt", "r")
    line = friend_file.readline()
    while line != "":
        friends.append(line.split())
        friends = list(filter(None, friends))  # To remove possibility of extra blank lines in file added to list
        network.__setitem__(friends[len(friends) - 1][0], 0) # Sets keys in friends with placeholder 0 for values
        line = friend_file.readline()
    friend_file.close()
except:
    print("A file error has occurred.")

"""To compute number of friends, simply count frequency that each name appears as mutual friendships are counted
for both people"""
count = 0  # Counts total friendships
for key in network:  # For each person, iterate over friends (the list storing all the data)
    for j in range(len(friends)):
        # Take the current person and each time their name appears in the list, increase the counter
        if key == friends[j][0] or key == friends[j][1]:
            count = count + 1
        ++j
    network.__setitem__(key, count)  # Update the value to show how many friends that person has
    count = 0
    print(key + " has " + str(network.__getitem__(key)) + " friends.")  # Prints out the person and their friend count
