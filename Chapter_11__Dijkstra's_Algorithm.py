# Dijkstra's Algorithm

# -> In the Breadth-first search we figured out how get from node A to node B in shortest path possible.
# Dijkstra's algorithm explains the fastest path to get from node A to node B when weight is added between 2 nodes.

# -> There are 4 steps to Dijkstra's algorithm -
# Find the cheapest node. This is the node you can ge in the least amount of time.
# Update the cost of the neighbors of this role.
# Repeat until you've done this for every node in the graph.
# Calculate the final path.

# Example -

#                 6            1
#           |---------> A ----->-----|
#           |           ^            |
# START ->  |           | 3          | -> Finish
#           |           |            |
#           |---------> B ----->-----|
#                 2            5

# -> Step 1
# Find the cheapest node. Starting from START, it takes 6 mins to go to A and 2 mins to go to B.
# Node B is the closest.

# Table -

#   NODE        TIME
#   Node A      6 min
#   Nobe B      2 min
#   Finish      Infinity

# Time taken to go to Finish node is infinity by default.

# Step 2 ->
# Taking node B as an edge, calculate how long it takes for neighbors of node B.
# Now, To node A it takes 5 mins and to Finish is 5 mins
# Now the shortest path to node A is only 5 mins down from 6 mins.

# Updated Table -

#   NODE        TIME
#   Node A      5 min
#   Nobe B      2 min
#   Finish      7 min

# Step 3 -> Repeat
# Step 1 again -
# Find the node that takes the least amount of time to get to, from node B, node A has the least amount of time to get to.

# Step 2 again -
# Update the cost for node A's neighbors.
# Now it takes only 6 mins to get to Finish
# Dijkstra algorithm has run for all nodes now.

# Updated Table -

#   NODE        TIME
#   Node A      5 min
#   Nobe B      2 min
#   Finish      2 min

# Implementation

# -> To code this you will need 3 hash tables - Graphs, Costs, Parents.
# Represent weights through hash tables.

graph = {}
graph["Start"] = {}
graph["Start"]["a"] = 6
graph["Start"]["b"] = 2

# -> graph["Start"] is a hash table and to see all the neighbors of Start -

print(graph["Start"].keys())

# -> There is an edge from Start to A and Start to B, to see the weight's for these edges -

print(graph["Start"]["a"])
print(graph["Start"]["b"])

# -> Rest of the Nodes and neighbors -

graph["a"] = {}
graph["a"]["Finish"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["Finish"] = 5

graph["Finish"] = {}

# -> Next we will need a hash table to store the cost of each node
# To store infinity for Finish we will store it as inf

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["Finish"] = infinity

# -> Hash tables for parents -

parents = {}
parents["a"] = "Start"
parents["b"] = "Start"
parents["Finish"] = None

# Array to keep track of all the node that are already processed.

processed = []

# The algorithm -

def find_lower_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lower_cost_node(costs)  # find the lowest cost node that you haven't processed yet
while node is not None:  # if you processed all the nodes this loop is done
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():  # go through all neighbors of this node
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:  # if its cheaper to get to this neighbor by this node ...
            costs[n] = new_cost  # ... update the cost of this node
            parents[n] = node  # this node becomes the parent of this neighbor
    processed.append(node)
    node = find_lower_cost_node(costs)  # finds the next node to process and loop

print(f"The most fastest rout from Start to Finish is - {processed}")

