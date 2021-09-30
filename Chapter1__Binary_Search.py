# Binary search

# -> Binary Search works on sorted arrays.
# Large data companies like Twitter, facebook often use binary search on their hash tables to find the data quickly.

# The binary search algorithm works as follows:
# -> Binary search begins by comparing the middle element of the array with the target value.
# -> If the target value matches the middle element, its position in the array is returned.
# -> If the target value is less than the middle element, the search continues in the lower half of the array.
# -> If the target value is greater than the middle element, the search continues in the upper half of the array.
# By doing this, the algorithm eliminates the half in which the target value cannot lie in each iteration.

# Example -

# -> Think of a number X between 1 and 100.
# -> Try to guess the number X with the fewest tries possible.
# -> With every guess you'll get hint such as - too low, too high or correct.
# -> Suppose you start guessing like: 1 (too low),2 (too low),3 (too low),4 (too low)......
# -> This is a simple search but with each guess you are only eliminating one number.
# -> If X was 99, you'll would take 99 tries to guess right.
# -> To search faster start with 50 ( halfway between 1 and 100 ).
# -> If 50 is too low, you just eliminated half the numbers. 1-50 -> too low.
# -> Now guess 75( halfway between 50 and 100 ).
# -> If 75 is too high, you eliminated 3/4 of the numbers.
# -> Next guess 63 ( halfway between 50 and 75 ). And so on.....

# Whatever the value of X, could be guessed in ony 7 tries using binary search.

# IMPORTANT -

# -> For a list of n values, binary search could take log(2)n steps to run in the worst case, whereas a simple search would take n steps.

# Logarithms -
# log(10)100 -> how many 10's do we multiply together to get 100.
# 10^2 = 100  --  log(10)100 = 2
# 2^3 = 8  --  log(2)8 = 3

# -> Binary search only works when you list is in sorted order.

# CODE SAMPLE -

# Finding a particular value in a list and its place value.

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


# sample list(must be sorted - lowest to highest)
my_list = [1, 3, 5, 7, 9]
# finding place value of #7
print(binary_search(my_list, 7))
# program will print 3 ( 7 has a place value of 3 as the place value of a list starts from 0 )
