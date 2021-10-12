# Hash Table -
# -> Suppose you work at a grocery store.
# When a customer buys produce, you have to look up the price in a book.
# If the book is unalphabetized, it can take you a long time to look through every single line for apple.
# You’d be doing a simple search, where you have to look at every line, which would take O(n) time.
# If the book is alphabetized, you could run binary search to find the price of an apple.
# That would only take O(log n) time.

# -> But as a cashier, looking things up in a book is a pain, even if the book is sorted.
# You can feel the customer steaming up as you search for items in the book.
# What you really need is a buddy who has all the names and prices memorized.
# Then you don’t need to look up anything: you ask her, and she tells you the answer instantly.

# -> Your buddy Maggie can give you the price in O(1) time for any item, no matter how big the book is. She’s even faster than binary search.

# -> What a wonderful person! How do you get a “Maggie”?
# Let’s put on our data structure hats. You know two data structures so far: arrays and lists.
# You could implement this book as an array

# -> Each item in the array is really two items: one is the name of a kind of produce, and the other is the price.
# If you sort this array by name, you can run binary search on it to find the price of an item.
# So you can find items in O(log n) time. But you want to find items in O(1) time.
# That is, you want to make a “Maggie.” That’s where hash functions come in.

# Hash Function -

# -> A hash function is a function where you put in a string1and you get back a number.

# -> In technical terminology, we’d say that a hash function “maps strings to numbers.”
# You might think there’s no discernable pattern to what number you get out when you put a string in.
# But there are some requirements for a hash function:

# • It needs to be consistent. For example, suppose you put in “apple” and get back “4”.
# Every time you put in “apple”, you should get “4” back.
# Without this, your hash table won’t work.

# • It should map different words to different numbers. For example, a hash function is no good if it always returns “1” for any word you put in.
# In the best case, every different word should map to a different number.

# So a hash function maps strings to numbers. What is that good for?
# Well, you can use it to make your “Maggie”!

# -> Start with an empty array:
# You’ll store all of your prices in this array. Let’s add the price of an apple.Feed “apple” into the hash function.
# The hash function outputs “3”. So let’s store the price of an apple at index 3 in the array.
# Let’s add milk. Feed “milk” into the hash function.he hash function says “0”. Let’s store the price of milk at index 0.
# Keep going, and eventually the whole array will be full of prices.

# -> Now you ask, “Hey, what’s the price of an avocado?” You don’t need to search for it in the array. Just feed “avocado” into the hash function.
# It tells you that the price is stored at index 4. And sure enough, there it is.

# -> The hash function tells you exactly where the price is stored, so you don’t have to search at all! This works because

# • The hash function consistently maps a name to the same index.Every time you put in “avocado”, you’ll get the same number back.
# So you can use it the first time to find where to store the price of an avocado, and then you can use it to find where you stored that price.

# • The hash function maps different strings to different indexes.
# “Avocado” maps to index 4. “Milk” maps to index 0. Everything maps to a different slot in the array where you can store its price.

# • The hash function knows how big your array is and only returns valid indexes.
# So if your array is 5 items, the hash function doesn’t return 100 … that wouldn’t be a valid index in the array.

# -> You just built a “Maggie”! Put a hash function and an array together, and you get a data structure called a hash table.
# A hash table is the first data structure you’ll learn that has some extra logic behind it.
# Arrays and lists map straight to memory, but hash tables are smarter.
# They use a hash function to intelligently figure out where to store elements.

# -> Hash tables are probably the most useful complex data structure you’ll learn.
# They’re also known as hash maps, maps, dictionaries, and associative arrays.
# And hash tables are fast! Remember You can get an item from an array instantly? And hash tables use an array to store the data, so they’re equally fast.

# -> You’ll probably never have to implement hash tables yourself. Any good language will have an implementation for hash tables.
# Python has hash tables; they’re called dictionaries. You can make a new hash table using the dict function:

book = dict()
book["apples"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.49


print(book)

# -> Pretty easy! Now let’s ask for the price of an avocado:

print(book["avocado"])
print(book["apples"])

# -> A hash table has keys and values. In the book hash, the names of produce are the keys, and their prices are the values.
# A hash table maps keys to values.
