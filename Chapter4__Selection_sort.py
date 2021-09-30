# SELECTION SORT

# -> TO understand selection sort you need to know arrays, lists and Big O notation.

# -> Suppose you have a list of movies with the their IMDB ratting in random order. You want to sort the movies from the highest ratting to the lowest.
# -> One way is go through the list and find the highest rated movie and add it to a new list.
# -> Do it again for the next highest rated movie.
# -> keep doing this and you will end up with a sorted list.

# Now lets find how long it will take to run this program.
# -> Running a simple search over the movie list is O(n).
# -> Now you have to run this simple search n time to get every movie.
# -> This will take O(n*n)times => O(n^2)times.

# Section sort is a neat algorithm but it is now the fastest. Quicksort is the fastest sorting algorithm that only takes O(n log(n)) -> explained in future chapter.

# Example code -

def findsmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# use the above function to write a selection sort:

def selectionsort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findsmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(findsmallest([5, 3, 7, 8, 2, 6, 4]))  # returns 4 as 2 is the smallest number in the list and is in the 4 position
print(selectionsort([5, 3, 7, 8, 2, 6, 4])) # will return [2, 3, 4, 5, 6, 7, 8], the list arranged from lowest to highest. 
