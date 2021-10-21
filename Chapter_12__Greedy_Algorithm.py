# The Classroom Scheduling Problem

# -> Suppose you have a classroom and you have to hold as many classes as possible.
# Here is a list of all the classes -

#   Classes     Start       End
#   ART         9:00am      10:00am
#   ENG         9:30am      10:30am
#   MATH        10:00am     11:00am
#   CS          10:30am     11:30am
#   MUSIC       11:00am     12:00pm

# -> All classes cant be held as there are some overlap between classes. An algorithm to hold as many classes as possible -

# 1) Pick a class that ends the soonest. (That will be your first class)
# 2) Pick a class that starts after the first class and ends sooner than others. (This will be your second class)
# 3) Repeat

# -> Algorithm run through -

# Going through the list the ART class ends the soonest at 10:00am. (First class - ART)
# Next class needs to start after 10:00am and end the soonest compared to others. ENG overlaps with the first class, but MATH starts at 10:00 and ends before the other classes. (Second class - MATH)
# Next class needs to be after 11:00am. CS overlaps but MUSIC works. (Third class - Music)

# -> A greedy algorithm is simple: at each step, pick the optimal move.
# In technical terms: at each step you pick the locally optimal solution.
# Greedy algorithms don't always work but they're simple to write.

# -> The Knapsack Problem

# -> Suppose you are a greedy thief and you are in a store to to steal stuff.
# Your knapsack can only hold 35lb.
# You are trying to maximize the value of of items to can take in you knapsack.
# A simple greedy algorithm -
# 1) Pick the most expensive thing that will fir in your knapsack.
# 2) pick the next most expensive that will fit in the knapsack, and so on.

# -> Suppose there are these three items to steal -
# 1) Stereo(30lbs) - $3000
# 2) Laptop(20lbs) - $2000
# 3) Guitar(15lbs) - $1500

# -> Since the knapsack can hold ony 35lbs, using the algorithm you can only steal the stereo as it is the most expensive item and no other item can be added due to the weight totaling at $3000.
# But if you would have taken the laptop and the guitar which would have fit in the knapsack, you could have $3500 worth of stuff.

# -> Greedy algorithm doesn't get you the optimal solution, but a pretty close one.
# Sometimes all you need is an algorithm that solves the problem pretty well.


# The Set-Covering Problem -

# -> Suppose you are starting a radio show. Tou want to reach listeners in all 50 states.
# You have to decide what stations to play on to reach all those listeners.
# It costs money for each station so you are minimize the number of station you play on. You have a list of stations.

#   Radio Station       Available In
#       KONE            ID, NV, UT
#       KTWO            WA,ID,MT
#       KTHREE          OR, NV, CA
#       KFOUR           NV, UT,
#       KFIVE           CA, AZ

# -> Each station covers a region, and there’s overlap.
# How do you figure out the smallest set of stations you can play on to cover all 50 states? Sounds easy, doesn’t it? Turns out it’s extremely hard.
# Here’s how to do it:
# 1. List every possible subset of stations.
# This is called the power set. There are 2^n possible subsets.
# 2. From these, pick the set with the smallest number of stations that
# covers all 50 states.

# -> The problem is, it takes a long time to calculate every possible subset of stations.
# It takes O(2^n) time, because there are 2^n stations.
# It’s possible to do if you have a small set of 5 to 10 stations.
# But with all the examples here, think about what will happen if you have a lot of items.
# It takes much longer if you have more stations. Suppose you can calculate 10 subsets per second.

# Approximation Algorithms

# -> Here’s a greedy algorithm that comes pretty close:
# 1. Pick the station that covers the most states that haven’t been covered yet.
# It’s OK if the station covers some states that have been covered already.
# 2. Repeat until all the states are covered.This is called an approximation algorithm.
# When calculating the exact solution will take too much time, an approximation algorithm will work.
# Approximation algorithms are judged by
# • How fast they are
# • How close they are to the optimal solution

# -> Greedy algorithms are a good choice because not only are they simple to come up with, but that simplicity means they usually run fast, too.
# In this case, the greedy algorithm runs in O(n^2) time, where n is the number of radio stations.





