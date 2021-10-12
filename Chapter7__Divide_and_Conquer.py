# Divide and Conquer

# This can be explained easily using this example -

# -> Suppose you’re a farmer with a plot of land.
#
#           |------------------------------------------|
#           |                                          |
#           |                                          |
#           |                                          |  640 m
#           |                                          |
#           |                                          |
#           |------------------------------------------|
#                               1680 m

# -> You want to divide this farm evenly into square plots. You want the plots to be as big as possible.


# -> How do you figure out the largest square size you can use for a plot of land? Use the D&C strategy! D&C algorithms are recursive algorithms.

# -> To solve a problem using D&C, there are two steps:
# 1. Figure out the base case. This should be the simplest possible case.
# 2. Divide or decrease your problem until it becomes the base case.

# -> Let’s use D&C to find the solution to this problem.
# What is the largest square size you can use?
# First, figure out the base case. The easiest case would be if one side was a multiple of the other side.

# -> Now you need to figure out the recursive case. This is where D&C comes in.
# According to D&C, with every recursive call, you have to reduce your problem.

# -> You can fit two 640 × 640 boxes in there, and there’s some land still left to be divided.
# Now here comes the “Aha!” moment.
# There’s a farm segment left to divide. Why don’t you apply the same algorithm to this segment?

# -> So you started out with a 1680 × 640 farm that needed to be split up.
# But now you need to split up a smaller segment, 640 × 400.
# If you find the biggest box that will work for this size, that will be the biggest box that will work for the entire farm.
# You just reduced the problem from a 1680 × 640 farm to a 640 × 400 farm!

# -> Let’s apply the same algorithm again. Starting with a 640 × 400m farm, the biggest box you can create is 400 × 400 m.

# -> And that leaves you with a smaller segment, 400 × 240 m.

# -> And you can draw a box on that to get an even smaller segment, 240 × 160 m.

# -> And then you draw a box on that to get an even smaller segment.

# ->  you’re at the base case: 80 is a factor of 160. If you split up this segment using boxes, you don’t have anything left over!

# -> So, for the original farm, the biggest plot size you can use is 80 × 80 m.

# Recursive example -

def Arr_Sum(list):
    a = len(list)
    if len(list) == 1:          # <-- Base case
        return list[0]
    else:               # <--Recursive case
        return list[0] + sum(list[1:])

print(Arr_Sum([1,4,8]))


