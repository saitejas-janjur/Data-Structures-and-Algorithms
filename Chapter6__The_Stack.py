# The stack

# -> This section covers the call stack. It’s an important concept in programming.
# The call stack is an important concept in general programming, and it’s also important to understand when using recursion.

# -> As an example take a todo list made up of sticky notes, You could add todo items anywhere to the list or delete random items.
# The stack of sticky notes is much simpler.
# When you insert an item, it gets added to the top of the list.
# When you read an item, you only read the topmost item, and it’s taken off the list.
# So your todo list has only two actions: push (insert) and pop (remove and read)

# -> This data structure is called a stack. The stack is a simple data structure.

# THE CALL STACK

# -> Your computer uses a stack internally called the call stack.
# Here is a simple example -


def greet_name(name):
    print("Hello " + name.title() + "!")
    greet2(name)
    bye()


def greet2(name):
    print("Hello " + name.title() + ", How are you ?")


def bye():
    print("Ok Bye!")


greet_name("sai tejas")


# -> Suppose you call greet(“sai tejas”). First, your computer allocates a box of memory for that function call.
#  now lets use that memory. The variable name is to "sai tejas". That needs to be saved in memory.
#  Every time you make a function call, your computer saves the values for all the variables for that call in memory like this.
#  Next, you print hello, Sai Tejas! Then you call greet2(“sai tejas”).
#  Again, your computer allocates a box of memory for this function call.
#  Now the topmost box on the stack is for the greet function, which means you returned back to the greet function.
#  When you called the greet2 function, the greet function was partially completed.
#  This is the big idea behind this section: when you call a function from another function, the calling function is paused in a partially completed state.
#  All the values of the variables for that function are still stored in memory.
#  Now that you’re done with the greet2 function, you’re back to the greet function, and you pick up where you left off.
#  First you print getting ready to say bye…. You call the bye function.
#  A box for that function is added to the top of the stack.
#  Then you print ok bye! and return from the function call.

# -> And you’re back to the greet function. There’s nothing else to be done,
# so you return from the greet function too. This stack, used to save the
# variables for multiple functions, is called the call stack.


# The call stack with recursion

# -> Recursive functions use the call stack too! Let’s look at this in action with the factorial function.
# factorial(5) is written as 5!, and it’s defined like this: 5! = 5 * 4 * 3 * 2 * 1. Similarly, factorial(3) is 3 * 2 * 1.
# Here’s a recursive function to calculate the factorial of a number -

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


print(fact(3))

# -> Now you call fact(3). Let’s step through this call line by line and see how the stack changes.
# Remember, the topmost box in the stack tells you what call to fact you’re currently on.

#   CODE                |    CALL STACK
#  ---------------------|---------------
#   fact(3)             |    fact: x=3
#  ---------------------|---------------
#   if x == 1           |    fact: x=3
#  ---------------------|---------------
#   else:               |    fact: x=3
#  ---------------------|---------------
#   return x*fact(x-1)  |    fact: x=2  <- This is the recursive call
#                       |    fact: x=3
#  =====================|===============
#   if x == 1           |    fact: x=2 <- This is the second call where fact x = 2. The topmost function call is the call we are currently in.
#                       |    fact: x=3
#  ---------------------|---------------
#   else:               |    fact: x=2 <- Both function calls have a variable names x, but the value of x is different in both.
#                       |    fact: x=3
#  ---------------------|---------------
#   return x*fact(x-1)  |    fact: x=1
#                       |    fact: x=2
#                       |    fact: x=3
#  =====================|===============
#   if x == 1           |    fact: x=1
#                       |    fact: x=2
#                       |    fact: x=3
#  ---------------------|---------------
#   return 1            |    fact: x=1 <- This is the first box to get popped off the stack, which means it is the call we return from
#                       |    fact: x=2
#                       |    fact: x=3
#  ---------------------|---------------
#   return x*fact(x-1)  |    fact: x=2 <- Returns 2
#                       |    fact: x=3
#  =====================|===============
#   return x*fact(x-1)  |    fact: x=3 <- Returns 6

# -> Notice that each call to fact has its own copy of x.
# You can’t access a different function’s copy of x.

# -> The stack plays a big part in recursion.
