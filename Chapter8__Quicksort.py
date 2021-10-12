# Quicksort

# -> Quicksort is a sorting algorithm.
# It’s much faster than selection sort and is frequently used in real life.
# For example, the C standard library has a function called qsort, which is its implementation of quicksort.
# Quicksort also uses D&C.

# Let’s use quicksort to sort an array

# -> Empty arrays and arrays with just one element will be the base case.
# You can just return those arrays as is—there’s nothing to sort:

def quicksort(array):
    if len(array) < 2:
        return array


print(quicksort([8]))


# -> Let’s look at bigger arrays. An array with two elements is pretty easy to sort, too.
# Check if the first element is smaller than the second element, if not swap them.

# -> Not for 3 elements and more -

# -> Remember, you’re using D&C.
# So you want to break down this array until you’re at the base case.
# Here’s how quicksort works. First, pick any element from the array.
# This element is called the PIVOT.

# ARRAY = [8,5,6,4,2,3]
# PIVOT = 5

# -> Now find the elements smaller than the pivot and the elements larger than the pivot.

# Numbers smaller than 5 = [4,2,3]
# Numbers larger than 5 =[8,6]
# Now the array looks like this =
# [4,2,3]           [5]         [8,6]
# Smaller than      Pivot       Larger than

# -> This is called partitioning. Now you have -
# • A sub-array of all the numbers less than the pivot
# • The pivot
# • A sub-array of all the numbers greater than the pivot
# The two sub-arrays aren’t sorted. They’re just partitioned.
# But if they were sorted, then sorting the whole array would be pretty easy.

# -> If the sub-arrays were sorted, then you can combine the whole thing like this —
# left array + pivot + right array —and you get a sorted array.
# In this case, it’s [2,3,4] + [5] + [6,8] = [2,3,4,5,6,8], which is a sorted array.

# -> How do you sort the sub-arrays? Well, the quicksort base case already
# knows how to sort arrays of three elements (the left sub-array) and 2 elements (the right sub-array).
# So if you call quicksort on the two sub-arrays and then combine the results, you get a sorted array!

# quicksort([4,2,3]) + [5] + quicksort([8,6])
# => [2,3,4,5,6,8]   <- Sorted array

# Code for Quicksort function -

def quicksort(array):
    if len(array) < 2:
        return array  # <- Base case
    else:
        pivot = array[0]  # <- Recursive case
        less = [i for i in array[1:] if i <= pivot]  # <- Sub array for all elements less than the pivot
        greater = [i for i in array[1:] if i > pivot]  # <- Sub array for all elements greater than the pivot

        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([8, 5, 6, 4, 2, 3]))
