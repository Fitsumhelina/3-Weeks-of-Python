
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


### Python Operators: Notes for Teaching

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