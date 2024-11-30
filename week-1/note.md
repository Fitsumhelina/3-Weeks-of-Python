
---

# Python syntax: 

## Statements

### Definition:
A **statement** is a unit of code that the Python interpreter can execute. It can either be a **simple statement** (one line) or a **compound statement** (multiple lines).

### Example of a Simple Statement:
```python
x = "HELLO WORLD"  # Assigning a string to the variable x
print(x)           # Printing the value of x
```

---

## Indentation

### Definition:
Python uses **indentation** to define the structure of blocks, unlike other programming languages that use curly braces `{}` or keywords like `begin` and `end`. Consistent indentation is **crucial** for Python's readability and to avoid errors.

### Example:
```python
if 3 > 2:  
    print("3 is greater than 2")  # This is part of the block
else:
    print("Nothing")             # This is part of another block
```

### **Note:**
If the indentation is inconsistent, Python will raise an `IndentationError`.

---

## Variables

### Definition:
Variables are containers for storing data values. In Python, you don't need to declare the type of variable explicitly. The type is inferred based on the assigned value.

### Example:
```python
x = 10         # Integer
name = "Alice" # String

print(x)       # Output: 10
print(name)    # Output: Alice
```

---

## Comments

### Definition:
Comments are used to describe and explain the code, making it more understandable. In Python, comments start with a `#` symbol and extend to the end of the line.

### Example:
```python
# This is a single-line comment
x = 10  # Inline comment
```

### **Note:**
Comments are ignored by the Python interpreter and do not affect the execution of the code.

---

## Conditional Statements

### Definition:
Conditional statements allow decision-making in the code. Python provides:
- **if**: Executes a block of code if the condition is `True`.
- **elif**: Checks additional conditions if the previous ones are `False`.
- **else**: Executes a block of code if all conditions are `False`.

### Example:
```python
mark = 60

if mark > 50:
    print("Pass")  # Output: Pass
elif mark < 50:
    print("Fail")
else:
    print("Nothing")
```

### **Note:**
Make sure variables like `mark` are defined before using them, or you will encounter a `NameError`.

---

## Loops

### Definition:
Loops are used to repeatedly execute a block of code as long as a condition is true.

### **For Loop:**
Used to iterate over sequences (e.g., lists, ranges).
```python
tech_tonic = ["Alice", "Bob", "Charlie"]

for student in tech_tonic:
    print(student)  # Prints each student's name
```

### **While Loop:**
Used to repeat a block of code as long as a condition is true.
```python
counter = 0

while counter < 5:
    print(counter)  # Output: 0, 1, 2, 3, 4
    counter += 1
```

---

## Loop Control Statements

### Definition:
Control the flow of loops.

1. **break**: Exits the loop.
2. **continue**: Skips the current iteration and continues with the next.

### Example:
```python
for i in range(10):
    if i == 5:
        continue  # Skip the current iteration when i == 5
    if i > 7:
        break  # Exit the loop when i > 7
    print(i)  # Output: 0, 1, 2, 3, 4, 6, 7
```

---

## Functions

### Definition:
Functions are reusable blocks of code that perform specific tasks. They help organize code and make it more maintainable.

### Example:
```python
def greet(name):
    print(f"Hello, {name}!")  # f-string for dynamic output

greet("Fitsum")  # Output: Hello, Fitsum!
```

---

## Modules and Imports

### Definition:
Modules are Python files containing Python code. You can import them into your scripts to use their functionality.

### Example:
```python
import math

# Using math module
print(math.sqrt(16))  # Output: 4.0
```

### **Note:**
Popular modules include:
- **math**: Mathematical operations.
- **pandas**: Data analysis.
- **numpy**: Numerical computations.

---

## Output in Python

### Example of Output:
```python
# Using print()
print("Welcome to Tech Tonic Tribe!")  # Output: Welcome to Tech Tonic Tribe!

# Using f-string for dynamic output
name = "Abebe"
print(f"Welcome {name}, how are you today?")  # Output: Welcome Abebe, how are you today?
```

---

## Input in Python

### Example of Taking User Input:
```python
name = input("Enter your name: ")  # Takes input from the user
print(f"Hello, {name}!")          # Outputs: Hello, <name>!
```

### **Note:**
`input()` always returns a string. If you need a number, you must convert it:
```python
age = int(input("Enter your age: "))
print(f"You are {age} years old.")
```

---

---

# Variables in Python

## What are Variables?

Variables are containers for storing data values. Python variables do not require explicit declaration, and a variable is created the moment you assign a value to it.

---

### Creating Variables

Python has no specific command to declare a variable. A variable is created by assigning a value to it.

```python
x = 5      # x is an integer
y = "John" # y is a string

print(x)   # Output: 5
print(y)   # Output: John
```

---

### Dynamic Typing in Python

Variables in Python are **dynamically typed**, meaning their type can change after assignment.

```python
x = 4       # x is of type int
x = "Sally" # x is now of type str

print(x)    # Output: Sally
```

---

### Casting Variables

To explicitly set a variable's type, use **casting**.

```python
x = str(3)    # x will be '3' (string)
y = int(3)    # y will be 3 (integer)
z = float(3)  # z will be 3.0 (float)

print(x, y, z)  # Output: '3', 3, 3.0
```

---

### Checking the Type of a Variable

You can determine a variable's data type using the `type()` function.

```python
x = 5
y = "John"

print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'str'>
```

---

### String Variables: Single or Double Quotes?

String variables can use either single or double quotes.

```python
x = "John"
y = 'John'

print(x)  # Output: John
print(y)  # Output: John
```

---

### Variable Name Case-Sensitivity

Variable names in Python are **case-sensitive**.

```python
a = 4       # 'a' is a separate variable
A = "Sally" # 'A' is a separate variable

print(a)  # Output: 4
print(A)  # Output: Sally
```

---

## Variable Names

### Rules for Naming Variables:

1. Must start with a **letter** or an **underscore (`_`)**.  
2. Cannot start with a number.  
3. Can only contain **alphanumeric characters** and **underscores** (A-Z, a-z, 0-9, `_`).  
4. Are **case-sensitive** (e.g., `age`, `Age`, and `AGE` are different).  
5. Cannot use Python **keywords** (like `if`, `while`, `return`, etc.).

### Examples:

#### Legal Variable Names:
```python
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
```

#### Illegal Variable Names:
```python
2myvar = "John"  # Starts with a number
my-var = "John"  # Contains a hyphen (-)
my var = "John"  # Contains a space
```

---

## Multi-Word Variable Names

For readability, use these conventions for multi-word variable names:

### 1. **Camel Case**
The first word is lowercase; each subsequent word starts with an uppercase letter.
```python
myVariableName = "John"
```

### 2. **Pascal Case**
Every word starts with an uppercase letter.
```python
MyVariableName = "John"
```

### 3. **Snake Case**
Words are separated by underscores.
```python
my_variable_name = "John"
```

---

## Assigning Values to Variables

### Assigning Multiple Values to Multiple Variables:
Python allows assigning multiple values to multiple variables in a single line.

```python
x, y, z = "Orange", "Banana", "Cherry"

print(x)  # Output: Orange
print(y)  # Output: Banana
print(z)  # Output: Cherry
```

### Assigning One Value to Multiple Variables:
You can assign the same value to multiple variables in a single line.

```python
x = y = z = "Orange"

print(x)  # Output: Orange
print(y)  # Output: Orange
print(z)  # Output: Orange
```

---

## Local and Global Variables

### Global Variables:
Variables declared outside a function are **global** and can be accessed both inside and outside of functions.

### Local Variables:
Variables declared inside a function are **local** and can only be used within that function.

### Example:
```python
x = "awesome"  # Global variable

def myfunc():
    x = "fantastic"  # Local variable
    print("Python is " + x)

myfunc()  # Output: Python is fantastic
print("Python is " + x)  # Output: Python is awesome
```

### **Note:**
The global variable `x` remains unchanged outside the function.

---

# Data Types

---

## Dynamic Typing in Python

Python does not require explicit declaration of a variable's data type. The data type is automatically determined when you assign a value.

---

### Data Types and Examples

Here are some examples of how Python sets the data type based on the value assigned:

```python
x = "Hello World"          # str
x = 20                     # int
x = 20.5                   # float
x = True                   # bool
x = ["apple", "banana"]    # list
x = ("apple", "banana")    # tuple
x = {"name": "John", "age": 36}  # dict
x = {"apple", "banana"}    # set
```

---

## Casting in Python

Sometimes, you may need to specify the data type explicitly. This is done using **constructor functions**:

- `int()`: Converts to an integer.
- `float()`: Converts to a floating-point number.
- `str()`: Converts to a string.

### Examples

#### Integers:
```python
x = int(1)       # x will be 1
y = int(2.8)     # y will be 2
z = int("3")     # z will be 3
```

#### Floats:
```python
x = float(1)       # x will be 1.0
y = float(2.8)     # y will be 2.8
z = float("3")     # z will be 3.0
w = float("4.2")   # w will be 4.2
```

#### Strings:
```python
x = str("s1")    # x will be 's1'
y = str(2)       # y will be '2'
z = str(3.0)     # z will be '3.0'
```

---

## Summary

- Python's dynamic typing simplifies variable assignment.
- Use `type()` to check the data type of any object.
- Use casting (`int()`, `float()`, `str()`) to convert data types when necessary.

Here’s the reformatted content in Markdown for teaching purposes, including notes and coding examples:


# Python Strings
---

## String Length

To get the length of a string, use the `len()` function.

### Example:

```python
a = "Hello, World!"
print(len(a))  # Output: 13
```

---

## Checking Strings

You can check if a specific phrase or character is present in a string using the `in` keyword.

### Examples:

```python
txt = "The best things in life are free!"
print("free" in txt)  # Output: True
```

```python
# Using `if` condition:
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")  # Output: Yes, 'free' is present.
```

---

## String Slicing

You can extract a portion of a string using slicing.  
The syntax is: `string[start:end]`.  
The `start` index is inclusive, and the `end` index is exclusive.

### Examples:

```python
b = "Hello, World!"
print(b[2:5])  # Output: llo (characters from index 2 to 4)

print(b[:5])   # Output: Hello (characters from start to index 4)

print(b[2:])   # Output: llo, World! (characters from index 2 to end)

print(b[-5:-2])  # Output: orl (characters from the 5th last to the 3rd last)
```

---

## String Methods

### Converting Case

- `upper()`: Converts all characters to uppercase.
- `lower()`: Converts all characters to lowercase.

**Examples:**

```python
a = "Hello, World!"
print(a.upper())  # Output: HELLO, WORLD!

print(a.lower())  # Output: hello, world!
```

---

### Replacing Strings

You can replace a substring with another string using `replace()`.

**Example:**

```python
a = "Hello, World!"
print(a.replace("H", "J"))  # Output: Jello, World!
```

---

## String Concatenation

You can combine two strings using the `+` operator.

**Examples:**

```python
a = "Hello"
b = "World"
c = a + b
print(c)  # Output: HelloWorld
```

To add a space between them:

```python
a = "Hello"
b = "World"
c = a + " " + b
print(c)  # Output: Hello World
```

---

## Combining Strings and Numbers

You cannot directly combine strings and numbers. Attempting this will raise an error.

**Incorrect Example:**

```python
age = 36
txt = "My name is John, I am " + age
print(txt)  # This will raise a TypeError.
```

To fix this, use `str()` to convert the number into a string:

```python
age = 36
txt = "My name is John, I am " + str(age)
print(txt)  # Output: My name is John, I am 36
```

---

## Summary

- Strings are versatile in Python and come with a variety of methods.
- Use slicing, concatenation, and methods like `upper()`, `lower()`, and `replace()` for string manipulation.
- Remember to convert non-strings to strings when combining them with text.


# Python Operators

This note serves as a reference for Python operators, grouped by type, with explanations and examples to help learners understand their functionality.

---

### **Arithmetic Operators**
Arithmetic operators are used for basic mathematical operations.

| Operator | Description         | Example   | Result |
|----------|---------------------|-----------|--------|
| `+`      | Addition            | `5 + 3`   | `8`    |
| `-`      | Subtraction         | `5 - 3`   | `2`    |
| `*`      | Multiplication      | `5 * 3`   | `15`   |
| `/`      | Division            | `10 / 2`  | `5.0`  |
| `%`      | Modulus             | `10 % 3`  | `1`    |
| `**`     | Exponentiation      | `2 ** 3`  | `8`    |
| `//`     | Floor Division      | `10 // 3` | `3`    |

**Example Code:**
```python
x = 10
y = 3
print(x + y)  # Addition: 13
print(x - y)  # Subtraction: 7
print(x * y)  # Multiplication: 30
print(x / y)  # Division: 3.333...
print(x % y)  # Modulus: 1
print(x ** y) # Exponentiation: 1000
print(x // y) # Floor Division: 3
```

---

### **Assignment Operators**
Assignment operators assign values to variables.

| Operator | Syntax    | Equivalent To   |
|----------|-----------|-----------------|
| `=`      | `x = 5`   | Assign value    |
| `+=`     | `x += 3`  | `x = x + 3`     |
| `-=`     | `x -= 3`  | `x = x - 3`     |
| `*=`     | `x *= 3`  | `x = x * 3`     |
| `/=`     | `x /= 3`  | `x = x / 3`     |
| `%=`     | `x %= 3`  | `x = x % 3`     |
| `//=`    | `x //= 3` | `x = x // 3`    |
| `**=`    | `x **= 3` | `x = x ** 3`    |

**Example Code:**
```python
x = 5
x += 3  # x = x + 3
print(x)  # Output: 8
x *= 2  # x = x * 2
print(x)  # Output: 16
```

---

### **Comparison Operators**
Comparison operators compare two values and return a boolean (`True` or `False`).

| Operator | Description                   | Example  | Result |
|----------|-------------------------------|----------|--------|
| `==`     | Equal to                      | `5 == 5` | `True` |
| `!=`     | Not equal to                  | `5 != 3` | `True` |
| `>`      | Greater than                  | `5 > 3`  | `True` |
| `<`      | Less than                     | `5 < 3`  | `False`|
| `>=`     | Greater than or equal to      | `5 >= 3` | `True` |
| `<=`     | Less than or equal to         | `5 <= 3` | `False`|

**Example Code:**
```python
a = 10
b = 5
print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a <= b)  # False
```

---

### **Logical Operators**
Logical operators combine multiple conditional statements.

| Operator | Description                                      | Example                    | Result |
|----------|--------------------------------------------------|----------------------------|--------|
| `and`    | Returns `True` if both statements are true       | `x < 5 and x < 10`         | `True` |
| `or`     | Returns `True` if at least one statement is true | `x < 5 or x < 4`           | `True` |
| `not`    | Reverses the result of the condition             | `not(x < 5 and x < 10)`    | `False`|

**Example Code:**
```python
x = 4
print(x > 2 and x < 5)  # True
print(x > 5 or x < 10)  # True
print(not(x > 3 and x < 5))  # False
```

---

### **Operator Precedence**
Python evaluates expressions based on operator precedence, as follows:

1. **Parentheses**: `()`
2. **Exponentiation**: `**`
3. **Unary operators**: `+x`, `-x`, `~x`
4. **Multiplication, Division, Modulus, Floor Division**: `*`, `/`, `%`, `//`
5. **Addition and Subtraction**: `+`, `-`
6. **Bitwise shifts**: `<<`, `>>`
7. **Bitwise AND**: `&`
8. **Bitwise XOR**: `^`
9. **Bitwise OR**: `|`
10. **Comparisons, Identity, Membership**: `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `is not`, `in`, `not in`
11. **Logical NOT**: `not`
12. **Logical AND**: `and`
13. **Logical OR**: `or`

**Example:**
```python
result = 2 + 5 * 6 / 2  # 2 + (5 * 6) / 2
print(result)  # Output: 17.0
```
---

# Python Conditions 

Python provides a flexible and intuitive way to make decisions using conditional statements. Below is a comprehensive guide, including examples, explanations, and tips.

---

## **Logical Conditions in Python**
Python supports the usual logical conditions used in mathematics:

1. **Equals:** `a == b`  
2. **Not Equals:** `a != b`  
3. **Less than:** `a < b`  
4. **Less than or equal to:** `a <= b`  
5. **Greater than:** `a > b`  
6. **Greater than or equal to:** `a >= b`  

---

### **The `if` Statement**

The `if` statement allows you to execute a block of code if a condition evaluates to `True`.

#### Example:

```python
a = 33
b = 200

if b > a:
    print("b is greater than a")
```

**Explanation:**
- Here, `b` is greater than `a` (`200 > 33`), so the condition is `True`, and the message `"b is greater than a"` is printed.

---

### **Indentation**

Python uses **indentation** (whitespace at the beginning of a line) to define the block of code under the `if` statement. Unlike many other languages, Python does not use curly braces `{}`.

#### Example with Correct Indentation:

```python
a = 33
b = 200

if b > a:
    print("b is greater than a")
```

#### Example Without Indentation (Raises an Error):

```python
a = 33
b = 200

if b > a:
print("b is greater than a")  # Incorrect indentation
```

---

### **The `elif` Statement**

The `elif` keyword stands for "else if." It allows you to check multiple conditions in a sequence.

#### Example:

```python
a = 33
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
```

**Explanation:**
- Here, the first condition `b > a` is `False`.
- The second condition `a == b` is `True`, so `"a and b are equal"` is printed.

---

### **The `else` Statement**

The `else` keyword catches any case that isn’t covered by previous conditions.

#### Example:

```python
a = 200
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
```

**Explanation:**
- Both `if` and `elif` conditions are `False`, so the `else` block is executed, and `"a is greater than b"` is printed.

---

### **Short Hand `if`**

If you have only one statement to execute, you can write the `if` statement in a single line.

#### Example:

```python
a = 200
b = 33

if a > b: print("a is greater than b")
```

---

### **Short Hand `if ... else`**

You can write an `if ... else` statement in a single line. This is also known as a **ternary operator** or **conditional expression**.

#### Example:

```python
a = 2
b = 330

print("A") if a > b else print("B")
```

**Explanation:**
- If `a > b`, `"A"` is printed; otherwise, `"B"` is printed.

#### Example with Multiple Conditions:

```python
a = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B")
```

**Explanation:**
- If `a > b`, `"A"` is printed.
- If `a == b`, `"="` is printed.
- Otherwise, `"B"` is printed.

---

### **Logical Operators**

Python provides logical operators to combine multiple conditions:

#### **`and` Operator**

The `and` operator ensures all conditions are `True` for the block to execute.

#### Example:

```python
a = 200
b = 33
c = 500

if a > b and c > a:
    print("Both conditions are True")
```

#### **`or` Operator**

The `or` operator executes the block if **at least one condition** is `True`.

#### Example:

```python
a = 200
b = 33
c = 500

if a > b or a > c:
    print("At least one of the conditions is True")
```

---

### **Nested `if` Statements**

You can nest `if` statements inside each other to create more complex conditions.

#### Example:

```python
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
```

**Explanation:**
- The outer `if` checks if `x > 10` (True).
- The nested `if` checks if `x > 20` (True), so `"and also above 20!"` is printed.

---

### **The `pass` Statement**

The `pass` statement is used when an `if` statement requires a block of code but you want to leave it empty for now. Without `pass`, Python will throw an error.

#### Example:

```python
a = 33
b = 200

if b > a:
    pass  # Placeholder to avoid errors
```

---

## **Key Takeaways**
1. **Indentation is mandatory:** Indentation defines the scope of blocks.
2. **Logical operators (`and`, `or`)** allow combining conditions.
3. Use **`elif`** to add multiple conditions and **`else`** to handle unmatched cases.
4. The **short-hand if-else** is a convenient way to write compact conditions.
5. **Nested conditions** enable complex logic, but keep readability in mind.
6. **`pass`** is a useful placeholder for empty blocks.

---

## **Practice Problems**

1. Write a program that checks whether a number is positive, negative, or zero.
2. Create a program that prints "Eligible to vote" if the age is 18 or above, otherwise prints "Not eligible."
3. Write a nested `if` program to check whether a number is divisible by 2 and also by 5.

---

# Python Loops

Python provides two main types of loops for iterating over data or executing a block of code repeatedly:

1. **`for` Loops**  
2. **`while` Loops**

N.B : python do not have do while loop support !


Below is a detailed guide on how to use these loops, including examples, tips, and best practices.

---

## **1. `for` Loops**

The `for` loop is used for iterating over sequences, such as lists, tuples, dictionaries, sets, or strings. It allows you to execute a block of code once for each item in the sequence.

### **Syntax:**

```python
for variable in sequence:
    # Code block
```

---

### **Examples of `for` Loops**

#### **Example 1: Looping Through a List**
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
**Output:**
```
apple
banana
cherry
```

---

#### **Example 2: Looping Through a String**
```python
for letter in "banana":
    print(letter)
```
**Output:**
```
b
a
n
a
n
a
```

---

#### **Example 3: Using a `range()` Function**

The `range()` function generates a sequence of numbers.

- **Syntax:** `range(start, stop, step)`
  - `start`: Starting number (default is 0)
  - `stop`: The end of the range (exclusive)
  - `step`: Increment (default is 1)

```python
for x in range(1, 10):  # Loop from 1 to 9
    print(x)
```

**Output:**
```
1
2
3
4
5
6
7
8
9
```

---

#### **Example 4: Looping Through Numbers 1–100**
```python
for num in range(1, 101):  
    print(num)
```

---

## **2. `while` Loops**

A `while` loop continues to execute as long as its condition is `True`.

### **Syntax:**

```python
while condition:
    # Code block
```

---

### **Examples of `while` Loops**

#### **Example 1: Basic While Loop**
```python
i = 1
while i < 6:
    print(i)
    i += 1  # Increment to avoid an infinite loop
```
**Output:**
```
1
2
3
4
5
```

**Note:** Always ensure the loop has an **increment or termination condition** to avoid infinite loops.

---

### **Break and Continue Statements**

These statements allow finer control over loop execution.

#### **The `break` Statement**

The `break` statement is used to exit a loop before its natural termination.

**Example: Exit When `i == 3`**
```python
i = 1
while i < 6:
    print(i)
    if i == 3:
        break  # Exit the loop
    i += 1
```
**Output:**
```
1
2
3
```

---

#### **The `continue` Statement**

The `continue` statement skips the rest of the code in the current iteration and moves to the next iteration.

**Example: Skip When `i == 3`**
```python
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue  # Skip the iteration
    print(i)
```
**Output:**
```
1
2
4
5
6
```

---

## **Key Differences Between `for` and `while` Loops**

| Feature                | `for` Loop                           | `while` Loop                    |
|------------------------|---------------------------------------|----------------------------------|
| **Purpose**            | Iterates over sequences or ranges.   | Runs until a condition is false.|
| **Use Case**           | Known iteration count or sequence.   | Unknown iteration count.        |
| **Example**            | Iterating over a list or range.      | Looping until a condition is met.|

---

## **Practice Problems**

1. Write a `for` loop to print all even numbers from 1 to 20.
2. Use a `while` loop to calculate the sum of numbers from 1 to 50.
3. Write a program that loops through a list of numbers and prints "Skip" if the number is 5, using `continue`.
4. Create a program that breaks out of a loop when a randomly generated number is greater than 90.

These notes provide a foundation for understanding and using loops in Python effectively!
