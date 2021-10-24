# K - Nearest Neighbors

# Classifying oranges vs. grapefruit -

# -> If there is a fruit and you don't know if it is a orange or a grapefruit.
# I know that a grapefruit is bigger and bit red.
# To use the K - Nearest Neighbors (KNN) to find if the fruit is an orange or a grapefruit, we have to draw a graph and plot orange and grapefruit based on color and size.

#     X |                      G     G
#       |                  G       G   G
#       |       O     X
#       |  O      O
#       |      O
#       |  O
#   ------------------------------------------- Y

# -> X measures the color of the frits from orange to red
# -> Y measures the size of the fruits from small to big
# -> X represents the unknown fruit

# -> To classify fruit X as an orange or a grapefruit we should look at its closest neighbors.
# Notice that X has 2 orange neighbors and only 1 grapefruit neighbor.
# Using KNN we just classified fruit X as a orange.
# KNN is a simple algorithm but a very useful one.

# Building a Recommendation System -

# -> If Netflix wanted to build a recommendations system for its users, on a high level it would look like the grapefruit problem.
# Plot every user on a graph by similarity, so that users with similar taste are plotted closely together.
# If you wanted to recommend a movie to user X, you find the users closest to user X.
# If you the user closest to user x like a movie, there is a good chance that user X might like that movie too.

# Feature Extraction -
# -> In the grapefruit example you compared fruits on how big and red they were.
# Size and color are the features you are comparing.
# Suppose you have these 3 fruits that you are comparing -
# 1) Fruit 1 - Size: 2, Redness: 2
# 1) Fruit 2 - Size: 2, Redness: 4
# 1) Fruit 3 - Size: 1, Redness: 5

#     X |
#       |                  C
#       |
#       |
#       |     A
#       |     B
#   ---------------------------------- Y

# -> From the graph ypu can tell that A and B are similar, now lets try to find the distance between them.
# We use the Pythagorean formula - Square Root of((X1 - X2)^2 + (Y1-Y2)^2)
# Here is the distance between A and B - Square Root of((2 - 2)^2 + (2-1)^2) => 1
# The distance between A and B is 1.

# -> Suppose your comparing Netflix's users, you need to graph them.
# To graph them ypu need to convert them into coordinate points just like the fruit example.
# Once you have the graph you can find the distance between users.
# Here's how you can convert users to numbers -
# -> When users signup for netflix, have them rate some categories of movies based on how many they like those likes, for each user have a set of ratings.

#               User-1      User-2      User-3
# Comedy        3           4           2
# Action        4           3           5
# Drama         4           5           1
# Horror        1           1           3
# Romance       4           5           1

# -> To compare 2 people with 5 Data Points, we use the same Pythagorean formula with 5 variables -
# => Square Root of((A1 - A2)^2 + (B1-B2)^2 + (C1-C2)^2 + (D1-D2)^2 + (E1-E2)^2)
# The distance formula is flexible, you can calculate the distance even if you have a million data points.
# Now to calculate the distance between user 1 and user 2 -
# => Square Root of((3 - 4)^2 + (4-3)^2 + (4-5)^2 + (1-1)^2 + (4-5)^2) = 2

# Regression -

# -> Suppose you want to do more than just recommend a movie, you want to guess how much will User-1 will rate this move
# You can take the five closest people to User-1 (you can take any number of people near to User-1, not only 5)
# Lets say if movie XYZ was rated 5,4,4,5,3 by the closest 5 users then the average of those numbers will be the predicted rating that User-1 will give for that movie.
# so the predicted rating will be - 4.2

















