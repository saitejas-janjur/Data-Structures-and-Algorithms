# Memory of a computer

# -> Each time you wanna store an item in memory, you ask the computer for some space, the computer gives you a location where you can sore that item.
# -> If you have to store multiple items, the 2 basic way of storing them are - Arrays and Lists.

# Arrays and Linked List -

# How memory works when using ARRAYS  -

# -> When you use an array all items in your array are stored continuously (right next to each other) in memory.
# -> If you want to store 3 elements in an array, the computer searched for 3 memory slots right next to each other.
# |__SLOT1___|__SLOT2___|__SLOT3___|__SLOT4___|__SLOT5___|__SLOT6___|__SLOT7___|___
# |_ELEMENT1_|_ELEMENT2_|_ELEMENT3_|__________|__________|__________|__________|___
#  { YOUR 3 ELEMENTS IN THE ARRAY }      {MEMORY IN USE FOR SOMETHING ELSE}
# -> Now if you want to add a new item to you existing array (making it 4 elements total) , the computer cannot cannot just add it next the 3rd element because that location is taken by some other application.
# -> Not the computer has to find another location which has 5 open memory slots open right next to each other.

# -> If you're out of space and need to move to a new spot in memory every time for adding a new element, it slows down your program.
# -> One easy fix is to "Hold Seats", you can ask the computer to hold X number of slots. (X = any number)
# -> Then you can add X items to you array without having to move.
# This is a good work around but, some of the downsides are -
# -> You may not need all the slots you reserved, you are not using it and neither can anything else be stored in those slots. It is a waste of memory.
# -> You may add more that X items and have to move anyway.

# -> This is a good work around but not the perfect solution. Linked Lists solve the problem of adding items.

# LINKED LISTS -

# -> With Linked Lists, items can be stores anywhere in memory.
# -> Each item stores the address of the next item. A bunch of random memory address are linked together.
# -> Its like a treasure hunt - you go to the first items address, and it says, go to location 123.
# After getting 2nd item in location 123, it say go to location 456 for 3rd item, and so on ......

# ARRAYS -

# -> In a linked list it is not possible to read the last element because you don't know the address of that element.
# The only way to know is to go to the first element, get the address for element 2. Then go to element 2, get the location address for element 3 and so on...

# -> Arrays are different, in an array you always know the location of all items.
# -> Location of item 1 is 00, location of item 2 is 01 and item 3 is 03 and so on..
# -> The elements in an array are numbers starting from 0.

# Example array -
# 10  20  30  40  50
#  0   1   2   3   4

# In this array the location of 20 is 1.

# -> The position of an element is called "Index". Instead of saying 20 is at location 1, you say 20 is at index 1.

# RUN TIMES FOR COMMON OPERATIONS ON LISTS AND ARRAYS.

#            ARRAYS    LISTS
# Reading     O(1)     O(n)
# Inserting   O(n)     O(1)

# O(1) -> Constant time
# O(n) -> Linear time

# INSERTING INTO THE MIDDLE OF A LIST

# -> If you want to add an element into the middle of a list, which is better? list ot array?
# -> With list, you only need to change the address in the previous element. But in an array you have to shift all the rest of the elements down.
# And if there is no space, you might have to copy everything to a new location.

# -> Lists are better if you want to insert elements into the middle.

# DELETIONS -

# -> If you want to delete an item, lists are better because only the location address in the previous element needs to change.
# -> Insertions can fail sometimes when there is not enough space, but an element can always be deleted.

# RUN TIMES FOR COMMON OPERATIONS ON LISTS AND ARRAYS.

#            ARRAYS    LISTS
# Reading     O(1)     O(n)
# Inserting   O(n)     O(1)
# Deletion    O(n)     O(1)

# O(1) -> Constant time
# O(n) -> Linear time













