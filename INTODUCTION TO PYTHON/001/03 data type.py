'''                 Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Boolean Type:	bool

'''

'''Getting the Data Type
You can get the data type of any object by using the type() function:

'''
# x = 5
# print(type(x))


''' cool thing in python   it doesn't need explicit the data type declaretion Setting the Data Type
In Python, the data type is set when you assign a value to a variable:

Example	Data Type	Try it'''


# x = "Hello World"	#str	
# x = 20	#int	
# x = 20.5	#float	
# x = True	#bool	
# x = ["apple", "banana", "cherry"]	#list	
# x = ("apple", "banana", "cherry")	#tuple	
# x = {"name" : "John", "age" : 36}	#dict	
# x = {"apple", "banana", "cherry"}	#set	


'''Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
ExampleGet your own Python Server
Integers:
'''
# x = int(1)   # x will be 1
# y = int(2.8) # y will be 2
# z = int("3") # z will be 3
'''Example
Floats:'''

# x = float(1)     # x will be 1.0
# y = float(2.8)   # y will be 2.8
# z = float("3")   # z will be 3.0
# w = float("4.2") # w will be 4.2

'''Example
Strings:
'''
# x = str("s1") # x will be 's1'
# y = str(2)    # y will be '2'
# z = str(3.0)  # z will be '3.0'