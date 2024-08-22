'''         Python Set

A set is a container (also called collection) that is unordered and immutable.
Creating a Set
A set is created by using curly brackets {}.
The objects are placed inside those brackets and are separated by commas (,).'''

# pets = {"dog", "cat", "rabbit"}
# print(pets)

'''A set can contain mixed data types, but can NOT contain mutable items like lists, sets and dictionaries.'''

# x = {"dog", 21, True}
# print(x)

'''
Accessing Items

Unlike lists and tuples, you can NOT access the items of a set using indexes.

It is because a set is unordered and not indexed.

However, we can use the for loop to access all its items one-by-one.'''

# pets = {"dog", "cat", "rabbit"}
# for pet in pets:
#     print(pet)

'''Adding Items to a Set

To add items to a set, use the add() or update() method.

The add() method adds one item to a set.'''

# pets = {"dog", "cat", "rabbit"} 
# pets.add("fish")
# print(pets)

'''
Changing an Item
The items of a set can NOT be changed because a set is immutable or unchangeable.'''

# pet=("cat","dog")
# pet[0]="cow"
# print(pet)

'''
Removing an Item
To remove an item from a set, use the remove() method.
You should specify the value of the item you want to remove.
'''

# pets = {"dog", "cat", "rabbit"} 
# pets.remove("rabbit")
# print(pets)

'''You can also use the discard() method.'''

# pets = {"dog", "cat", "rabbit"}
# pets.discard("rabbit")
# print(pets)

'''
The difference between the remove() and discard() method is that the 
discard() method does not raise an error if the specified item is not present.
You can also use the pop() method to remove an item.
But we cannot determine which item will be removed because a set is unordered.
'''
# pets = {"dog", "cat", "rabbit", "hamster"}
# pets.pop()
# print(pets)

'''Getting the Length of a Set
To get the length or the number of items in a set, use the len() method.'''

# pets = {"dog", "cat", "rabbit"}
# print(len(pets)) #3

'''Checking if an Item Exists
To check if an item exists in a set, use the in operator.
It returns True if the item is found, otherwise returns False.'''

# pets = {"dog", "cat", "rabbit"}
# print("dog" in pets) #True
# print("python" in pets) # False
'''
Combine Two Sets
To combine two sets, we can use the update() method.
This method excludes duplicate items.'''

# x= {1, 2, 3, 4}
# y = {4, 5, 6}
# x.update(y)
# print(x)

'''
Difference of Two Sets
To get the difference between two sets, use the subtraction operator (-).'''

# x= {1, 2, 3, 4}
# y = {3, 4, 5, 6}
# print("x-y:", x-y)  # the result will be a new set containing elements that are in x but not in y
# print("y-x:", y-x)  # the result will be a new set containing elements that are in y but not in x


'''Another Way to Create a Set

The way we created our sets above is called literal.

Another way to create a set is to use the set() constructor.'''

# pets = set(("dog", "cat", "rabbit"))     #take note of the double brackets
# print(pets)


# Exercise 1
# Print all the values from the cars set using a for loop.

# cars = "toyota", "honda", "ford" for car
# print()

# Exercise 2
# Add "tesla" to the set of cars.

# cars = "toyota", "honda", "ford" ("tesla")
# print(cars)





