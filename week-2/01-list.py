'''Python List

A python list is an ordered container.

A list is created by using square brackets ([]).

The objects are placed inside those brackets and are separated by commas (,).'''


# pets = ["dog", "cat", "rabbit"]

# print(pets)



# A list can contain mixed data types.

# x = ["dog", 21, True]

# print(x)



# Indexing

'''Indexing is used to access the items of a list.

Indexing uses square brackets and numbers to access individual items of a list.

Where 0 refers to the first item, 1 refers to the second item, and so on.

'''
# pets = ["dog", "cat", "rabbit"]

# print(pets[0])

# print(pets[1])

# print(pets [2])

'''           Negative Indexing

Negative indexing is used to access the items of a list using negative numbers.

Where -1 refers to the last item, -2 refers to the second to the last item, and so on.'''

# pets = ["dog", "cat", "rabbit"]

# print(pets[-1])

# print(pets[-2])

# print(pets[-3])

'''

                      Range of Indexes

By using a colon (:), we can access a range of items at once.

Simply separate two indexes using the colon.

The first index is the start of the range, while the second index is the end of the range (not included).
'''
# pets = ["dog", "cat", "rabbit", "fish", "hamster"] x = pets [1:3] # ['cat', 'rabbit']

# print(x)



# If you don't specify the first index, the range starts from index 0.

# pets = ["dog", "cat", "rabbit", "fish", "hamster"]
# x = pets[:2] # ['dog', 'cat']
# print(x)





'''If you don't specify the last index, the range ends with the last item of the list.

In this case, the range includes the last item.'''

# pets = ["dog", "cat", "rabbit", "fish", "hamster"]
# x = pets [2:] # ['rabbit', 'fish', 'hamster']

# print(x)



'''Adding Items to a List

The append() method adds an item to the end of the list.

In this example, we will add "rabbit" to our pets list.'''

# pets = ["dog", "cat"] 
# pets.append("rabbit")
# print(pets)

'''
The insert() method inserts an item at the specified index.
In this example, we will insert "rabbit" to index 0 and "hamster" to index 2.'''

# pets = ["dog", "cat", "fish"]

# pets.insert(0, "rabbit")

# pets.insert(2, "hamster")

# print(pets)

# print(pets[0]) # access index 0

# print(pets [2]) # access index 2


'''
Deleting Items from a List

The pop() method removes the last item from a list.'''

# pets = ["dog", "cat", "rabbit"]

# pets.pop()

# print(pets)


'''The remove() method removes the specified item value.'''

# pets = ["dog", "cat", "rabbit"]

# pets.remove("cat")

# print(pets)

'''To delete a specified index, use the del keyword.'''

# pets = ["dog", "cat", "rabbit"] 
# del pets[2]
# print(pets)
'''

Getting the Length of a List

To get the length or the number of items in a list, use the len() method.
'''

# pets = ["dog", "cat", "rabbit"]
# print(len(pets)) #3

'''

Changing an Item's Value

To change an item's value, access the index first and use the assignment operator.'''

# pets = ["dog", "cat", "rabbit"]
# pets[2] = "fish"
# print(pets)


'''Checking if an Item Exists

To check if an item exists in a list, use the in operator.

It returns True if the item is found, otherwise returns False.'''

# pets = ["dog", "cat", "rabbit"]
# print("dog" in pets) #True
# print("python" in pets) # False



'''Extending a List

The extend() method adds all items from a list to another list.
'''

# nums1= [1, 2, 3]
# nums2=[4, 5, 6]
# nums1.extend(nums2)
# print(nums1)


'''
Looping Through a List

Looping through a list basically means accessing all its items one-by-one.

The for loop is used to loop through a list.'''

# pets = ["dog", "cat", "rabbit"]
# for pet in pets: print(pet)


'''Another Way to Create a List

The way we created our lists above is called literal.

Another way to create a list is to use the list() constructor.

'''

# pets = list(("dog", "cat", "rabbit"))
#take note of the double brackets
# print(pets)  


# -----------------------------------------------------------------------------------------------
# Exercise 1
# Create a list of cars, then print it.

# cars =  "toyota", "honda", "ford"
# print (cars)

# Exercise 2
# Print "toyota" from the list of cars.

# cars = ["toyota", "honda", "ford"] 
# print()





