'''Python Tuple

Python tuple is an ordered container.

Yes, it's the same as lists but the items of tuples cannot be changed.

Note! The term "items" can also be referred to as "elements".

Creating a Tuple

A tuple is created by using round brackets ().

The objects are placed inside those brackets and are separated by commas (,).'''

# pets =("dog", "cat", "rabbit")
# print(pets)

'''A tuple can contain mixed data types.'''

# x = ("dog", 21, True)
# print(x)

'''
Indexing

Indexing is used to access the items of a tuple.

Indexing uses square brackets and numbers to access individual items of a tuple.

Where 0 refers to the first item, 1 refers to the second item, and so on.'''

# pets =("dog", "cat", "rabbit")
# print(pets[0])
# print(pets[1])
# print(pets[2])

'''
Negative Indexing

Negative indexing is used to access the items of a tuple using negative numbers.

Where -1 refers to the last item, -2 refers to the second to the last item, and so on.
'''

# pets = ("dog", "cat", "rabbit")
# print(pets[-1])
# print(pets[-2])
# print(pets[-3])

'''
Range of Indexes

By using a colon (:), we can access a range of items at once.

Simply separate two indexes using the colon.

The first index is the start of the range, while the second index is the end of the range (not included).'''

# pets =("dog", "cat", "rabbit", "fish", "hamster") 
# x = pets [1:3] # ('cat', 'rabbit')
# print(x)


'''If you don't specify the first index, the range starts from index 0.'''

# pets =("dog", "cat", "rabbit", "fish", "hamster") 
# x = pets[:2] # ('dog', 'cat')
# print(x)

'''
If you don't specify the last index, the range ends with the last item of the tuple.

In this case, the range includes the last item.
'''
# pets= ("dog", "cat", "rabbit", "fish", "hamster") 
# x = pets [2:] # ('rabbit', 'fish', 'hamster')
# print(x)

'''
Getting the Length of a Tuple

To get the length or the number of items in a tuple, use the len() method.
'''

# pets = ("dog", "cat", "rabbit")
# print(len(pets)) #3


'''
Looping Through a Tuple

Looping through a tuple basically means accessing all its items one-by-one.

The for loop is used to loop through a tuple.
'''
# pets ("dog", "cat", "rabbit")
# for pet in pets: print(pet)

'''
Checking if an Item Exists

To check if an item exists in a tuple, use the in operator.

It returns True if the item is found, otherwise returns False.'''

# pets ("dog", "cat", "rabbit")
# print("dog" in pets)
# #True
# print("python" in pets) # False

'''
Another Way to Create a Tuple

The way we created our tuples above is called literal.

Another way to create a tuple is to use the tuple() constructor.
'''

# take note of the double brackets
# pets tuple (("dog", "cat", "rabbit"))
# print(pets)

'''Combine Tuples
To combine tuples, use the addition operator (+).'''

# pets1= ("dog", "cat", "rabbit")
# pets2 = ("fish", "bird", "hamster")
# all_pets= pets1 + pets2
# print(all_pets)

'''Tuples are Immutable

In Python, tuples are immutable (unchangeable).

It means you can NOT add, remove or change its items.'''

# my_tuple = (1, 2, 3, 4, 5)
'''Attempt to change an item (this will raise an error)'''
# my_tuple[0] = 10 

'''Attempt to add an item (this will raise an error)'''
# my_tuple.append(6) 

'''Attempt to remove an item (this will raise an error)'''
# my_tuple.remove(3)  
