'''Python Dictionary

A dictionary is an unordered and mutable collection of items.
A dictionary is written with curly brackets.
Each item in a dictionary contais a key/value pair.
'''

# person = { "first_name": "John", "last_name": "Doe", "age": 30 }
# print(person)

''' In the example above we have 3 items:

The first item has a key name of "first_name" and its value is "John".

The second item has a key name of "last_name", and its value is "Doe".

The third item has a key name of "age", and its value is 30.'''

'''Accessing Items

To access an item, specify the key name of an item inside square brackets.'''

# person = { "first_name": "John", "last_name": "Doe", "age": 30 }
# x = person["first_name"]
# y = person ["last_name"]
# z = person["age"]
# print("First Name:", x)
# print("Last Name:", y)
# print("Age:", z)



'''If you try to access an item using a key name that does not exist, an error will be raised.'''

# person = {

# "first_name": "John",

# "last_name": "Doe",

# "age": 30

# }

# print(person["hobby"])   # this will raise an error


'''We can also use the get() method to access an item.'''

# person = {
# "first_name": "John",

# "last_name": "Doe",

# "age": 30
# }
# print(person.get("first_name"))

'''Instead of raising an error, the get() method will only return None if the specified key is not found.'''

# person = {

# "first_name": "John",

# "last_name": "Doe",
# "age": 30

# }
# print(person.get("hobby"))  # this will return None



'''
Adding Items

To add new items, specify a new index key name inside the square brackets and assign a value using the assignment operator.
'''
# person = {
# "first_name": "John",

# "last_name": "Doe",

# "age": 30
# }
# person["hobby"] = "playing basketball"
# print(person["hobby"]) 

'''
Changing an Item's Value

To change an item's value, refer to its key name using square brackets and use the assignment operator.'''

# person = {

# "first_name": "John",

# "last_name": "Doe",

# "age": 30

# }
# person ["first_name"] = "Jane" 
# print(person)


'''Removing an Item

To remove an item, use the pop() method.

The pop() method removes an item with the specified key name.'''

# person = {

# "first_name": "John",

# "last_name": "Doe",

# "age": 30

# }
# person.pop("age")
# print(person)


'''Another way to remove an item is to use the del keyword.'''

# person = {
# "first_name": "John",

# "last_name": "Doe",

# "age": 30
# }
# del person ["age"]
# print(person)


''' Getting the Length of a Dictionary

To get the length or the number of items in a dictionary, use the len() method.'''

# person = {

# "first_name": "John",

# "last_name": "Doe",

# "age": 30

# }
# print(len(person)) #3
'''
Checking if a Key Exists

To check if a key exists in a dictionary, use the in operator with the if statement.'''

# person = {
# "first_name": "John",

# "last_name": "Doe",

# "age": 30
# }
# if "age" in person: 
#     print('the "age" key exists')


'''Tip! You will learn about the if statement later in the course.

Looping Through a Dictionary

Looping through a dictionary basically means accesing its items one-by-one.

To do this, use the for loop.

The for loop returns the key name of each item, allowing us to access them one-by-one. '''

# person = {
# "first_name": "John",

# "last_name": "Doe",

# "age": 30
# }
# for key in person:
#     print(person [key])


'''Nested Dictionary

A dictionary can contain another dictionary.'''

# employees = {
    
# "manager": {
# "name": "Jane Doe",
# "age": 29
# },

# "programmer": {
# "name": "John Doe",
# "age": 30
# }

# }
# print(employees)

'''To access an item in a nested dictionary, access the key name of the dictionary then the key name of the item.'''

# employees = {

# "manager": {
# "name": "Jane Doe",
# "age": 29
# },

# "programmer": {
# "name": "John Doe",
# "age": 30
# }

# }
# print(employees ["manager"]["name"])
# print(employees ["programmer"]["name"])



# Exercise 1
# Create a person dictionary that contains a "first_name" and "last_name" items.

# person = {
# : "John", "Doe"
# }

# Exercise 2
# Print the "last_name" item from the person object.

# person = { 
#           "first_name": "John",
#           "last_name": "Doe"
# }

# print( )