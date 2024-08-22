
'''   Python Functions
A function is a group of statements that performs a particular task.

This function's task is simply to print Hello World!.'''

# def my_func(): 
#     x = "Hello World!"
#     print(x)
# my_func()

'''
Creating a Function

To create a function, we need the following:

1) The def keyword.

2) A function name.

3) Round brackets () and a colon

4) A function body a group of statements

5) indentation'''

# def my_func():
#     x = "love python programming"
#     print(x)   
# my_func()


'''Note! A group of statements must have the same indentation level, 
in the example above we used 2 whitespaces to indent the function body.
This example will produce an indentation error because the function body is not indented properly.'''

# def my_func():
# x = "love python programming" 
# print(x) # this produces an error
# my_func()

'''
Tip! It is up to you how many whitespaces you want to use to indent your function body.
Calling a Function

To execute a function, it needs to be called.

To call a function, use its function name with parentheses ().'''

# your_function_name()


'''
Function Parameters/Arguments

When calling a function, we can pass data using parameters/arguments.

A parameter is a variable declared in the function.

In this example, the hello() function has one parameter, the name parameter.'''

# def hello(name):
#     x = "Hello"
#     print(x, name)
# # Call the function
# hello("John")

'''
Multiple Parameters/Arguments

To use multiple parameters, separate them using commas.

The arguments when calling the function should also be separated by commas.'''

# def add_nums (num1, num2):
#     sum = num1 + num2 
#     print(sum)

# add_nums (4,3)


'''Note! You will get an error if you don't pass enough required arguments.'''

# def add_nums (num1, num2): 
#     sum = num1 + num2 
#     print(sum)
# # two arguments are requireo
# #but only one is passed
# add_nums (4)


'''
Default Arguments

A function can have default arguments.

It can be done using the assignment operator (=).

If you don't pass the argument, the default argument will be used instead.'''

# def hello(name="Paul"):
#     x = "Hello"
#     print(x, name)

# hello("John")
# hello()  # This will use the default value "Paul"



'''
Keyword Arguments

As you may notice, the arguments passed are assigned according to their postion.

When using keyword arguments, the position does not matter.'''

# def my_func(fruit1, fruit2, fruit3):
#     print("I love ", fruit1) 
#     print("I love ",fruit2)
#     print("I love ",fruit3)

# my_func(fruit3 = "banana", fruit2 = "apples", fruit1="orange")

''' The return Statement

The return statement is used to return a value to the function caller.'''

# def add_nums(num1, num2):
#     sum = num1 + num2  # Corrected syntax for calculating the sum
#     print("inside the function ")
#     return sum  # Returning the calculated sum
# print(add_nums(4, 3))
# print("outside of the function ")



# Another example:
# def add_nums (num1, num2):
#     sum= num1 + num2
#     return sum
# x = add_nums (4, 3) 
# print(x)

'''
Important! The return statement stops the execution of a function.

In this example, the print() function after the return statement will not be executed.
'''

# def add_nums (num1, num2):
#     sum = num1 + num2 
#     return sum 
# print("this string will not be printed")
# print(add_nums (4, 3))


# Exercise 1
# Properly indent this function using two whitespaces as the indentation level.

# def my_func():
# msg = "Hello World!"
# print(msg)
# my_func()


# Exercise 2
# Create a function called add_numbers that adds two numbers and returns its result.

# add_numbers(x, y)
# result = X + y
# return
# ()