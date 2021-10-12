# Recursion -

# -> Suppose you are digging through your grandma's attic and come across a mysterious locked suitcase.
# -> Grandma tells you that the key for the suitcase is probably in this other box.
# -> This box contains more boxes, with more boxes inside those boxes.
# -> The key is in there somewhere. What is your algorithm to find the key.

# ALGORITHM 1

# 1) Make a pile of boxes to look through
# 2) Grab a box and look through it.
# 3) If you get another box, add it to the pile and look through it later.
# 4) If you find the key, your done.
# 5) Repeat.

# ALGORITHM 2

# 1) Look through the boxes.
# 2) If you find a box, go to step 1.
# 3) If you find the key, your done.

# Which algorithm was easy ?


# ALGORITHM 1 CODE

# def Look_for_key(main_box):
#     pile = main_box.make_a_pile_to_look_through()
#     while pile is not empty:
#         box = pile.grab_a_box()
#         for item in box:
#             if item.is_a_box():
#                 pile.append(item)
#             elif item.is_a_key():
#                 print("found the key!")


# ALGORITHM 2 CODE

# def look_for_key(box):
#  for item in box:
#     if item.is_a_box():
#         look_for_key(item) # <----- This is recursion
#      elif item.is_a_key():
#         print("Found the key")

# -> The second algorithm uses recursion. RECURSION is where the function calls itself.

# -> Recursion is used when it makes the solution clearer.
# ->There’s no performance benefit to using recursion; in fact, loops are sometimes better for performance.
# -> Loops may achieve a performance gain for your program. Recursion may achieve a performance gain for your programmer.
# Choose which is more important in your situation.

# -> every recursive function has two parts: the base case, and the recursive case. The recursive case is when the function calls itself.
# ->The base case is when the function doesn’t call itself again … so it doesn't’t go into an infinite loop.

def countdown(i):
    print(i)
    if i <= 0:          # <-- Base case
        return 0
    else:               # <--Recursive case
        countdown(i - 1)


countdown(5)
