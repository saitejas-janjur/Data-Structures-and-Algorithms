# Run time

# -> Anytime you write an algorithm you need to be aware of the run time of the program.
# -> Generally you want to choose the most efficient algorithm whether you are trying to optimize for time and space.

# Linear Time -> Checking each number one by one. If a list has 4 billion numbers it would take 4 billion guesses, the maximum number of guesses are same as the size of the list. number of guesses = n  (where n in the number of items in a list
# Logarithmic Time (Log Time) -> In a binary search, if a list has 4 billion items it only takes 32 guesses, number of guesses = log(2)n  (where n in the number of items in a list)

#  Simple Search -> 100 Items - 100 Guess | 4 billion Items - 4 Billion Guess |      Linear Time - O(n)
# Binary Search - >  100 Items - 7 Guess  |     4 Billion Items - 32 Guess    | Logarithmic Time - O(Log m)

# Big O Notation -

# -> Big O Notation is a special notation that that represents how fast an algorithm is.
# -> Big O doesn't tell you the speed in seconds, it lets you compare the number if operations. It tells you how fast the algorithm grows.
# Example - Binary search needs log(n) operations to check a list of size n, the runtime in Big O Notation is - O(log n).

# Big O establishes a worst case runtime  -
# -> Using simple search to look for a person in a phone book, the runtime will be O(n), which means that in the worst case you'll have to go through every single entry in the phone book.

# Common Big O runtime -
# -> O(log n) - log time - Binary search
# -> O(n) - linear time - simple search
# -> O(n * log n) - slow sorting algorithm like quick sort (explained in later chapter)
# -> O(n!) - a really slow algorithm

