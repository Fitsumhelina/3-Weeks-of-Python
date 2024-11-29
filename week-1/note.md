
---

# Python syntax: Statements, Variables, Indentation, and More

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