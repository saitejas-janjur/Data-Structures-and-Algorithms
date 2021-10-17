# -> Breadth first search allows you to find the shortest distance between two points.

# -> Breadth first search can be used to -
# find the shortest number of moves needed to solve a rubix cube.
# write a spell checker(fewer edits from your misspelling to a real)

# Introduction to graphs -

# What is a graph -

# -> A graph model is a set of connections.
# Suppose you and your friends are playing poker and you want to model who owes who money, you could say it like -
# Alex owes James
# James owes Tom
# I oww James and Tom

# Here's what that looks like in graph -

# Alex ------> James ------> Tom
#               ^             ^
#               |             |
#               |             |
#               |             |
#               Me ------------
#

# -> Graphs are made up of nodes and edges.
# A node can be directly connected to many other nodes.
# Those nodes are called its neighbors.
# In the graph James is Alex's neighbor. Tom is not Alex's neighbor because they are not directly connected.
# I am neighbors to James and Tom.

# -> Graphs are a way to model how different things are connected to one another.

# Breadth-First Search

# -> Like we used binary search algorithm to search a list of elements, Breadth-first search algorithm runs on graphs.

# -> Breadth-first search helps answer 2 questions -
# Is there a path from node A to node B?
# If so, what is the shortest path from node A to node B?

# -> Suppose you are a owner of a pet business and ou are looking for people with pets to advertise.
# First you make a list of your friends and see if they have any pets.
# If they don't have any pets, now make a list of your friends' friends.
# Each time you search someone in your list, add their friends to the end of the list.
# ( You add their friends to the end of the list is because you need to find the shortest path to your potential customer. There is a data structure for this - a queue)
# This way you not only search your friends, but you search their friends - and then their friends and so on.

# -> Using this you find the path for potential customers and at the same time you are finding the shortest connection.

# Queues -

# -> A queue works exactly like it does in real like.
# Suppose you are queueing up for a bus, the first person in the que get onto the bus first and then the second person and so on.
# Queues works the same way in CS.
# Queues are similar to stacks, you cant access random elements in the queue.
# Instead there are only 2 operations - enqueue and dequeue.
# If you enqueue two items to a list, the first item you added first will be dequeued before the second.

# Queue - First In First Out (FIFO)
# Stack - First In Last Out (FILO)

# Implementing a graph -

# -> A graph consists of several nodes and each node has neighboring node.
# We express this relation through a hashtable.
# A hash table allows you to map a key to a value and in this case we can map a node to its neighbors.

graph = {}
graph["Alex"] = ["James", "Tom"]

# -> Notice that "Alex" is mapped to an array. so graph["Alex"] will give an array of all neighbors of "Alex".

# Alex ------> James ------> Tom
#  ^   |        ^             ^
#  |   |        |             |
#  |   |        |         |---|
#  |   -------->Me -------|   Bob
#  |            ^              |
#  |            |              |
#  -----------------------------

# -> Lets see how map this complex graph.

graph = {}
graph["Alex"] = ["James", "Tom", "Me"]
graph["James"] = ["Tom"]
graph["Me"] = ["James", "Tom"]
graph["Bob"] = ["Me", "Alex"]

print(graph)

# -> It doesn't matter what order you enter the key/value pair. Hash table do not have any ordering so it does not matter.

# Implementing the algorithm -

# -> Recap of how the algorithm works -
# Make a queue containing your friends to check.
# pop the first person of the queue
# Check if that person has a pet.
# If yes, then you aew done.
# If No, add all their friends to the Queue.
# Now loop again.
# If queue is empty then no one has a pet in your network.

# -> To make a queue, lets use double-ended queue (dequeue)  function for this -

from collections import deque

def person_has_pet(name):
    return name[-1] == 'y'

def search_for_pets():
    graph = {}
    graph["you"] = ["Bob", "Claire", "Alice"]
    graph["Bob"] = ["Tom", "Peggy"]
    graph["Claire"] = ["Jonny", "Tim"]
    graph["Alice"] = ["Peggy"]

    search_queue = deque()
    search_queue += graph["you"]
    while search_queue:  # not empty
        person = search_queue.popleft()  # first person in the queue
        if person_has_pet(person):  # check if the person has pets
            print(f"{person} has pets.")  # yes they have pets
            return True
        else:
            search_queue += graph[person]  # no they don't have pets
    return False

print(search_for_pets())

# -> you will get an error because Tom doesn't have any friends. We need to make sure we pass people who have friends
# -> Alice and Bob have friend Peggy, Peggy will be added to the list twice.
# you ony need to check Peggy once to see if she is has pet.
# Before checking a person its important to  make sure they haven't checked already. To do that you'll keep a list of people you've already checked.

# Edited code bugs fixed -

def search_for_pets():
    graph = {}
    graph["you"] = ["Bob", "Claire", "Alice"]
    graph["Bob"] = ["Tom", "Peggy"]
    graph["Claire"] = ["Jonny", "Tim"]
    graph["Alice"] = ["Peggy"]

    search_queue = deque()
    search_queue += graph["you"]
    searched = []
    while search_queue:  # not empty
        person = search_queue.popleft()  # first person in the queue
        if person not in searched:
            if person_has_pet(person):  # check if the person has pets
                print(f"{person} has pets.")  # yes they have pets
                return True
            else:
                search_queue += graph[person]  # no they don't have pets
                searched.append(person)
    return False
print(search_for_pets())

# -> The runtime for Breadth-first algorithm is writen - O(V+E) (V- number of vertices(friends to search through in this case), E- number of edges(connections between friends))
