


'''                  Variables

Variables are containers for storing data values.

Creating Variables
Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.

ExampleGet your own Python Server'''

# x = 5
# y = "John"
# print(x)
# print(y)

'''Variables do not need to be declared with any particular type, and can even change type after they have been set.

Example'''

# x = 4       # x is of type int
# x = "Sally" # x is now of type str
# print(x)


'''Casting
If you want to specify the data type of a variable, this can be done with casting.

Example
'''
# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0


'''Get the Type
You can get the data type of a variable with the type() function.

Example'''

# x = 5
# y = "John"
# print(type(x))
# print(type(y))


'''You will learn more about data types and casting later in this tutorial.
Single or Double Quotes?
String variables can be declared either by using single or double quotes:

Example'''

# x = "John"
# # is the same as
# x = 'John'


'''Case-Sensitive
Variable names are case-sensitive.

Example
This will create two variables:
'''
# a = 4
# A = "Sally"
# #A will not overwrite a
# print (a)   #is differnt from 
# print (A) 



'''                                Variable Names

A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
ExampleGet your own Python Server'''


# Legal variable names:

# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"


# Illegal variable names:

# 2myvar = "John"
# my-var = "John"
# my var = "John"


'''Remember that variable names are case-sensitive



                              Multi Words Variable Names
                Variable names with more than one word can be difficult to read.

                There are several techniques you can use to make them more readable:'''

'''Camel Case
Each word, except the first, starts with a capital letter:'''

# myVariableName = "John"

'''Pascal Case
Each word starts with a capital letter:'''

# MyVariableName = "John"

'''Snake Case
Each word is separated by an underscore character:'''

# my_variable_name = "John"




'''         Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:

Example : '''


# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)



'''         One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:

Example'''

# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)



'''If you create a variable with the same name inside a function, this variable will be local, 
and can only be used inside the function. The global variable with the same name will remain as it was, 
global and with the original value.

Example
Create a variable inside a function, with the same name as the global variable'''

# x = "awesome" #global variable

# def myfunc():
#   x = "fantastic"   #local  variable
#   print("Python is " + x)   #it will print " python is fantastic "

# myfunc()

# print("Python is " + x)  #it will print " python is awesome"




