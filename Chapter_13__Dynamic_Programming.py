# Dynamic Programing

# -> Dynamic programming is the technique of solving a hard problem be breaking it into smaller sub-problems and solving them first.

# The Knapsack Problem -

# -> Lets use the same knapsack example from the last chapter.

# The simple Solution -

# -> The simple algorithm for this example would be to try every set of goods and find the one that gives you the most value.
# This would work good but it is really slow.
# For 3 items you have to calculate 8 different sets and for 4 items you have to calculate 16 different sets.
# Every item you add the number of sets double, this algorithm take O(2^n)time.

# Dynamic Programming -

# -> For the sake of this algorithm lets take a new weights for the items (You will understand why later). And the max weight the knapsack can hold is 4lbs.
# 1) Stereo(4lbs) - $3000
# 2) Laptop(3lbs) - $2000
# 3) Guitar(1lbs) - $1500

# -> For every dynamic-programming algorithm start with a grid. Here's the grid for the knapsack problem -

#                   1           2           3           4
#       Guitar
#       Stereo
#       Laptop

# -> Each row for each item and each column for the size of the knapsack(1-4lbs)
# The grid will start out empty and we will fill them out as we go.

# -> The Guitar Row

# In the guitar row we will be trying to fit the guitar into the knapsack.
# At each cell there is simple decision to make: Do you seal the guitar or not.
# The purpose of this algorithm is to find the set of items to steal that will give you the most value.
# The first cell has a knapsack capacity of 1 lb.
# The guitar weighs 1 lb, so that the only item that can fit into the first cell at a value of $1500.

#                   1           2           3           4
#       Guitar      $1500(G)
#       Stereo
#       Laptop

# Like this each cell in the grid will contain a list of items that can fit into the knapsack at that point.
# The next cell in has a capacity of 2 lbs and the guitar will definitely fit in there.

#                   1           2           3           4
#       Guitar      $1500(G)    $1500(G)
#       Stereo
#       Laptop

# The same goes for the rest of the cells in the row.
# Since this is the guitar row, you have ony the guitar to choose from and the other 2 items are not available yet.

#                   1           2           3           4
#       Guitar      $1500(G)    $1500(G)    $1500(G)    $1500(G)
#       Stereo
#       Laptop

# The cell on the first row represents the current best guess for the max value, which is $1500.

# -> The Stereo Row
# The second row is for the Stereo. In the second row you can steal both the Guitar and stereo.
# The max value currently in this column is $1500.
# Starting with the first cell, the knapsack currently has a max weight of 1 lb.
# Now should we steal the stereo or not? Since the max capacity of the knapsack is only 1 lb, there is space to add the stereo which is 4lbs.
# The max value of this cell remains $1500.

#                   1           2           3           4
#       Guitar      $1500(G)    $1500(G)    $1500(G)    $1500(G)
#       Stereo      $1500(G)
#       Laptop

# The same thing for the next 2 cell, the stereo will be to heavy to fit in the knapsack along with the guitar.
# So the max value will remain $1500 for cell 2 and 3.

#                   1           2           3           4
#       Guitar      $1500(G)    $1500(G)    $1500(G)    $1500(G)
#       Stereo      $1500(G)    $1500(G)    $1500(G)
#       Laptop

# Now for the 4th cell the max weight is 4lbs, the stereo finally fits.
# We will take the stereo and not the guitar because the value of the guitar was $1500 but now the value of the stereo is $3000.

#                   1           2           3           4
#       Guitar      $1500(G)    $1500(G)    $1500(G)    $1500(G)
#       Stereo      $1500(G)    $1500(G)    $1500(G)    $3000(S)
#       Laptop

# The Laptop Row
# The laptop weighs 3 lbs and will not fit in cell 1 or 2, and the max value in those will remain $1500.

#                   1           2           3           4
#       Guitar      $1500(G)    $1500(G)    $1500(G)    $1500(G)
#       Stereo      $1500(G)    $1500(G)    $1500(G)    $3000(S)
#       Laptop      $1500(G)    $1500(G)

# At 3lbs the old max value was $1500, but if we choose the laptop the new max value will be $2000.

#                   1           2           3           4
#       Guitar      $1500(G)    $1500(G)    $1500(G)    $1500(G)
#       Stereo      $1500(G)    $1500(G)    $1500(G)    $3000(S)
#       Laptop      $1500(G)    $1500(G)    $2000(L)

# At 4lbs is where thighs get a bit interesting.
# The current max value is $3000, you can put the laptop but it is only $2000, which is less than the previous value.
# But the laptop only weighs 3lbs and you can add 1 more lb.
# Now we have been calculating the max value for 1lb of space all along.
# In the last row the max value for 1 lb is $1500, so now we can all a laptop plus a guitar for a total of 4lbs and a new max value of $3500.
#                   1           2           3           4
#       Guitar      $1500(G)    $1500(G)    $1500(G)    $1500(G)
#       Stereo      $1500(G)    $1500(G)    $1500(G)    $3000(S)
#       Laptop      $1500(G)    $1500(G)    $2000(L)    $3500(L+G)

# -> Dynamic programming is useful when you’re trying to optimize something given a constraint.
# In the knapsack problem, you had to maximize the value of the goods you stole, constrained by the size of the knapsack.

# You can use dynamic programming when the problem can be broken into discrete sub-problems, and they don’t depend on each other.

# ->  Some general tips follow:
# Every dynamic-programming solution involves a grid.
# The values in the cells are usually what you’re trying to optimize. For the knapsack problem, the values were the value of the goods.
# Each cell is a sub-problem, so think about how you can divide your problem into sub-problems. That will help you figure out what the axes are.



