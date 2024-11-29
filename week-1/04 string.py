'''Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:'''


# print("Hello")
# print('Hello')   # same damm thing 



'''String Length
To get the length of a string, use the len() function.

Example
The len() function returns the length of a string:'''

# a = "Hello, World!"
# print(len(a))  #the leng of the string is 13




'''Check String
To check if a certain phrase or character is present in a string, we can use the keyword in.

Example

Check if "free" is present in the following text:'''



# txt = "The best things in life are free!"
# print("free" in txt)


# or we can use as 

# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")
  
  
  
'''  
  Slicing
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

Example : 
Get the characters from position 2 to position 5 (not included):'''

# b = "Hello, World!"
# print(b[2:5])   # should print llo


# b = "Hello, World!"
# print(b[:5])   #should print Hello


# b = "Hello, World!"
# print(b[2:])


# b = "Hello, World!"
# print(b[-5:-2])


'''
The upper() method returns the string in upper case:
'''
# a = "Hello, World!"
# print(a.upper())

'''The lower() method returns the string in lower case:
'''
# a = "Hello, World!"
# print(a.lower())

'''The replace() method replaces a string with another string:
'''
# a = "Hello, World!"
# print(a.replace("H", "J"))

'''             String Concatenation
To concatenate, or combine, two strings you can use the + operator.

Example:
Merge variable a with variable b into variable c:'''

# a = "Hello"
# b = "World"
# c = a + b
# print(c)

# To add a space between them, add a " ":

# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)


'''
As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

Example:'''

# age = 36
# txt = "My name is John, I am " + age
# print(txt)


