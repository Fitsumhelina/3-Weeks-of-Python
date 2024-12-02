

![logo](./../image//week1.png)

# Cataloge
### 01 [python-lists](#01-python-lists)
### 02 [python-set](#02-python-set)
### 03 [python-tuple](#03-python-tuple)
### 04 [python-dictionary](#04-python-dictionary)
### 05 [python-functions](#05-python-functions)


---

# 01 Python Lists  

## **Introduction**  
A Python list is an **ordered, mutable collection** that can hold items of various data types. Lists are versatile and widely used in Python for data manipulation.  

---

## **1. Creating a List**  
### Syntax  
Use square brackets `[]` to define a list. Items are separated by commas `,`.  

**Examples**  
```python
# Simple list of strings
pets = ["dog", "cat", "rabbit"]
print(pets)

# List with mixed data types
mixed_list = ["dog", 21, True]
print(mixed_list)
```

### Using the `list()` Constructor  
```python
# Creating a list using the constructor
pets = list(("dog", "cat", "rabbit"))
print(pets)  # Output: ['dog', 'cat', 'rabbit']
```

---

## **2. Accessing List Elements**  
### **Indexing**  
List indexing starts at **0**. Use indices to access specific elements.  

**Examples**  
```python
pets = ["dog", "cat", "rabbit"]
print(pets[0])  # Output: dog
print(pets[2])  # Output: rabbit
```

### **Negative Indexing**  
Negative indices start from `-1` for the last item.  
```python
pets = ["dog", "cat", "rabbit"]
print(pets[-1])  # Output: rabbit
print(pets[-2])  # Output: cat
```

### **Range of Indexes**  
Use a colon `:` to access a range of items.  
```python
pets = ["dog", "cat", "rabbit", "fish", "hamster"]

# From index 1 to 3 (excluding 3)
print(pets[1:3])  # Output: ['cat', 'rabbit']

# Shortcut examples
print(pets[:2])  # Output: ['dog', 'cat']  # Start from beginning
print(pets[2:])  # Output: ['rabbit', 'fish', 'hamster']  # Till the end
```

---

## **3. Modifying Lists**  
### **Adding Items**  
#### Using `append()`  
Adds an item to the **end** of the list.  
```python
pets = ["dog", "cat"]
pets.append("rabbit")
print(pets)  # Output: ['dog', 'cat', 'rabbit']
```

#### Using `insert()`  
Adds an item at a **specific index**.  
```python
pets = ["dog", "cat", "fish"]
pets.insert(1, "rabbit")  # Insert at index 1
print(pets)  # Output: ['dog', 'rabbit', 'cat', 'fish']
```

### **Deleting Items**  
#### Using `pop()`  
Removes the last item (default) or an item at a specified index.  
```python
pets = ["dog", "cat", "rabbit"]
pets.pop()  # Remove last item
print(pets)  # Output: ['dog', 'cat']
```

#### Using `remove()`  
Deletes an item by value.  
```python
pets = ["dog", "cat", "rabbit"]
pets.remove("cat")
print(pets)  # Output: ['dog', 'rabbit']
```

#### Using `del` Keyword  
Deletes an item by index or clears the list.  
```python
pets = ["dog", "cat", "rabbit"]
del pets[1]  # Delete 'cat'
print(pets)  # Output: ['dog', 'rabbit']
```

---

## **4. Other Operations**  

### **Get the Length**  
```python
pets = ["dog", "cat", "rabbit"]
print(len(pets))  # Output: 3
```

### **Modify Item**  
```python
pets = ["dog", "cat", "rabbit"]
pets[2] = "fish"
print(pets)  # Output: ['dog', 'cat', 'fish']
```

### **Check for an Item**  
```python
pets = ["dog", "cat", "rabbit"]
print("dog" in pets)  # Output: True
```

### **Extend a List**  
```python
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums1.extend(nums2)
print(nums1)  # Output: [1, 2, 3, 4, 5, 6]
```

---

## **5. Looping Through a List**  
```python
pets = ["dog", "cat", "rabbit"]
for pet in pets:
    print(pet)
```

---

## **6. List Comprehension**  
An elegant way to create or modify lists.  
```python
# Create a list of squares
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]
```

---

## **Exercises**  

### **Easy**  
1. Create a list of five fruit names and print it.  
2. Access and print the last element in the list `["apple", "banana", "cherry"]`.  
3. Add `"kiwi"` to the list `["apple", "banana"]` and print the updated list.  
4. Remove `"banana"` from the list `["apple", "banana", "cherry"]`.  
5. Use a loop to print each item in the list `["cat", "dog", "fish"]`.  

### **Medium**  
1. Create a list of numbers from 1 to 10 and print only the even numbers.  
2. Reverse the list `["red", "green", "blue"]`.  
3. Combine the two lists `[1, 2, 3]` and `[4, 5, 6]` into one list.  
4. Modify the list `[5, 10, 15]` by replacing `10` with `12`.  
5. Find the length of the list `["a", "b", "c", "d"]` and print it.  

### **Hard**  
1. Use list comprehension to generate a list of squares for numbers from 1 to 10, excluding numbers divisible by 3.  
2. Create a nested list (matrix) and print the second row.  
3. Write a program to find duplicates in a list `[1, 2, 3, 2, 4, 5, 1]`.  
4. Sort the list `[3, 1, 4, 1, 5, 9]` in descending order without using the `sort()` method.  
5. Flatten a nested list `[[1, 2], [3, 4], [5, 6]]` into a single list `[1, 2, 3, 4, 5, 6]`.  

---

# 02 Python Set

### Introduction to Sets
A **set** in Python is an unordered collection of unique items. Sets are:
1. **Unordered**: Items do not have a defined order.
2. **Immutable (unchangeable)**: The items themselves cannot be changed, but you can add or remove items from the set.

---

### Creating a Set
To create a set, use curly brackets `{}` and separate the items with commas.

```python
# Example: Creating a set
pets = {"dog", "cat", "rabbit"}
print(pets)
```

A set can contain mixed data types, but **it cannot include mutable types** like lists, other sets, or dictionaries.

```python
# Example: Set with mixed data types
x = {"dog", 21, True}
print(x)
```

---

### Accessing Items
Sets do not support indexing or slicing because they are unordered. However, you can use a `for` loop to access each item.

```python
# Example: Looping through a set
pets = {"dog", "cat", "rabbit"}
for pet in pets:
    print(pet)
```

---

### Adding Items to a Set
You can add items to a set using:
1. The `add()` method to add a single item.
2. The `update()` method to add multiple items or merge another set.

```python
# Example: Adding an item with add()
pets = {"dog", "cat", "rabbit"}
pets.add("fish")
print(pets)

# Example: Adding multiple items with update()
pets.update(["hamster", "bird"])
print(pets)
```

---

### Changing an Item
You **cannot change items in a set** because they are immutable.

```python
# Example: Attempting to change an item (not allowed)
pets = {"dog", "cat"}
# pets[0] = "fish"  # This will raise an error
```

---

### Removing Items
You can remove items from a set using:
1. `remove()`: Raises an error if the item doesn't exist.
2. `discard()`: Does not raise an error if the item doesn't exist.
3. `pop()`: Removes an arbitrary item.

```python
# Example: Removing an item with remove()
pets = {"dog", "cat", "rabbit"}
pets.remove("cat")
print(pets)

# Example: Removing an item with discard()
pets.discard("rabbit")
print(pets)

# Example: Removing an arbitrary item with pop()
pets = {"dog", "cat", "rabbit"}
pets.pop()
print(pets)
```

---

### Checking the Length of a Set
To get the number of items in a set, use the `len()` method.

```python
# Example: Checking the length of a set
pets = {"dog", "cat", "rabbit"}
print(len(pets))  # Output: 3
```

---

### Checking if an Item Exists
Use the `in` operator to check for the existence of an item in a set.

```python
# Example: Checking for item existence
pets = {"dog", "cat", "rabbit"}
print("dog" in pets)  # Output: True
print("fish" in pets)  # Output: False
```

---

### Combining Two Sets
You can combine two sets using the `update()` method, which excludes duplicates.

```python
# Example: Combining sets
x = {1, 2, 3}
y = {3, 4, 5}
x.update(y)
print(x)  # Output: {1, 2, 3, 4, 5}
```

---

### Difference of Two Sets
To find the difference between two sets, use the subtraction operator `-`.

```python
# Example: Difference between sets
x = {1, 2, 3, 4}
y = {3, 4, 5, 6}
print(x - y)  # Output: {1, 2}
print(y - x)  # Output: {5, 6}
```

---

### Another Way to Create a Set
You can use the `set()` constructor to create a set. 

```python
# Example: Using the set() constructor
pets = set(("dog", "cat", "rabbit"))  # Double brackets
print(pets)
```

---

### Exercises
#### Exercise 1: Print All Items in a Set
```python
# Solution
cars = {"toyota", "honda", "ford"}
for car in cars:
    print(car)
```

#### Exercise 2: Add an Item to a Set
```python
# Solution
cars = {"toyota", "honda", "ford"}
cars.add("tesla")
print(cars)
```

---

# 03 Python Tuple

Python tuple is an **ordered container**.  

It is similar to lists, but the items in tuples cannot be changed.  

> **Note:** The term "items" can also be referred to as "elements".  

---

## Creating a Tuple  

A tuple is created using **round brackets ()**.  

The objects are placed inside those brackets and separated by commas (,).  

```python
# Example
pets = ("dog", "cat", "rabbit")
print(pets)
```

---

### Mixed Data Types  

A tuple can contain **mixed data types**.  

```python
# Example
x = ("dog", 21, True)
print(x)
```

---

## Indexing  

**Indexing** is used to access the items of a tuple.  

Indexing uses **square brackets** and numbers to access individual items.  

- `0` refers to the first item, `1` to the second, and so on.  

```python
# Example
pets = ("dog", "cat", "rabbit")
print(pets[0])  # Output: dog
print(pets[1])  # Output: cat
print(pets[2])  # Output: rabbit
```

---

## Negative Indexing  

**Negative indexing** is used to access items with negative numbers.  

- `-1` refers to the last item, `-2` to the second-to-last, and so on.  

```python
# Example
pets = ("dog", "cat", "rabbit")
print(pets[-1])  # Output: rabbit
print(pets[-2])  # Output: cat
print(pets[-3])  # Output: dog
```

---

## Range of Indexes  

Using a **colon (:)**, you can access a range of items.  

- The first index is the **start** of the range.  
- The second index is the **end** (not included).  

```python
# Example
pets = ("dog", "cat", "rabbit", "fish", "hamster")
x = pets[1:3]  # Output: ('cat', 'rabbit')
print(x)
```

### Omitting Start or End Index  

- If the **start index** is omitted, the range starts from `0`.  
```python
# Example
x = pets[:2]  # Output: ('dog', 'cat')
print(x)
```

- If the **end index** is omitted, the range ends with the last item.  
```python
# Example
x = pets[2:]  # Output: ('rabbit', 'fish', 'hamster')
print(x)
```

---

## Getting the Length  

To get the **length** or number of items in a tuple, use the `len()` method.  

```python
# Example
pets = ("dog", "cat", "rabbit")
print(len(pets))  # Output: 3
```

---

## Looping Through a Tuple  

To loop through a tuple and access all its items one-by-one, use a **for loop**.  

```python
# Example
pets = ("dog", "cat", "rabbit")
for pet in pets:
    print(pet)
```

---

## Checking if an Item Exists  

To check if an item exists in a tuple, use the **`in`** operator.  

- It returns `True` if the item is found, otherwise `False`.  

```python
# Example
pets = ("dog", "cat", "rabbit")
print("dog" in pets)  # Output: True
print("python" in pets)  # Output: False
```

---

## Another Way to Create a Tuple  

You can also create a tuple using the **`tuple()`** constructor.  

```python
# Example
pets = tuple(("dog", "cat", "rabbit"))  # Note the double parentheses
print(pets)
```

---

## Combine Tuples  

To combine two tuples, use the **addition operator (+)**.  

```python
# Example
pets1 = ("dog", "cat", "rabbit")
pets2 = ("fish", "bird", "hamster")
all_pets = pets1 + pets2
print(all_pets)  # Output: ('dog', 'cat', 'rabbit', 'fish', 'bird', 'hamster')
```

---

## Tuples are Immutable  

In Python, tuples are **immutable** (unchangeable).  

This means you cannot:  

- Change an item.  
```python
# Attempt to change an item (Raises an error)
my_tuple = (1, 2, 3)
my_tuple[0] = 10  
```

- Add an item.  
```python
# Attempt to add an item (Raises an error)
my_tuple.append(6)  
```

- Remove an item.  
```python
# Attempt to remove an item (Raises an error)
my_tuple.remove(3)  
```
---

# 04 Python Dictionary  

A dictionary is an unordered and mutable collection of items.  
A dictionary is written with curly brackets `{}`.  
Each item in a dictionary contains a **key/value** pair.  

```python
person = { "first_name": "John", "last_name": "Doe", "age": 30 }
print(person)
```

### Explanation  

In the example above, we have 3 items:  
1. The first item has a key name of `"first_name"` and its value is `"John"`.  
2. The second item has a key name of `"last_name"` and its value is `"Doe"`.  
3. The third item has a key name of `"age"` and its value is `30`.  

---

### Accessing Items  

To access an item, specify the key name of an item inside square brackets `[]`.  

```python
person = { "first_name": "John", "last_name": "Doe", "age": 30 }
x = person["first_name"]
y = person["last_name"]
z = person["age"]
print("First Name:", x)
print("Last Name:", y)
print("Age:", z)
```

---

### Handling Non-Existing Keys  

If you try to access a key that does not exist, an error will be raised:  

```python
person = { "first_name": "John", "last_name": "Doe", "age": 30 }
print(person["hobby"])  # KeyError
```

#### Use `get()` to Avoid Errors  

```python
person = { "first_name": "John", "last_name": "Doe", "age": 30 }
print(person.get("hobby"))  # None
```

---

### Adding Items  

To add new items, specify a new key name inside square brackets and assign a value:  

```python
person = { "first_name": "John", "last_name": "Doe", "age": 30 }
person["hobby"] = "playing basketball"
print(person)
```

---

### Changing an Item's Value  

To modify an item's value, refer to its key name and assign a new value:  

```python
person = { "first_name": "John", "last_name": "Doe", "age": 30 }
person["first_name"] = "Jane"
print(person)
```

---

### Removing Items  

#### Using `pop()`  

```python
person = { "first_name": "John", "last_name": "Doe", "age": 30 }
person.pop("age")
print(person)
```

#### Using `del`  

```python
person = { "first_name": "John", "last_name": "Doe", "age": 30 }
del person["age"]
print(person)
```

---

### Getting the Length of a Dictionary  

Use the `len()` method to get the number of items in a dictionary:  

```python
person = { "first_name": "John", "last_name": "Doe", "age": 30 }
print(len(person))  # 3
```

---

### Checking if a Key Exists  

To check if a key exists, use the `in` operator with an `if` statement:  

```python
person = { "first_name": "John", "last_name": "Doe", "age": 30 }
if "age" in person:
    print('The "age" key exists')
```

---

### Looping Through a Dictionary  

The `for` loop returns each key in the dictionary:  

```python
person = { "first_name": "John", "last_name": "Doe", "age": 30 }
for key in person:
    print(key, ":", person[key])
```

---

### Nested Dictionary  

A dictionary can contain another dictionary:  

```python
employees = {
    "manager": {
        "name": "Jane Doe",
        "age": 29
    },
    "programmer": {
        "name": "John Doe",
        "age": 30
    }
}
print(employees)
```

#### Accessing Nested Dictionary Items  

```python
employees = {
    "manager": {
        "name": "Jane Doe",
        "age": 29
    },
    "programmer": {
        "name": "John Doe",
        "age": 30
    }
}
print(employees["manager"]["name"])  # Jane Doe
print(employees["programmer"]["name"])  # John Doe
```

---

### Exercises  

**Exercise 1:** Create a `person` dictionary with "first_name" and "last_name" items:  
```python
person = { "first_name": "John", "last_name": "Doe" }
```

**Exercise 2:** Print the `"last_name"` item from the `person` dictionary:  
```python
person = { "first_name": "John", "last_name": "Doe" }
print(person["last_name"])
```
---
# 05 Python Functions

## **Introduction to Functions**
A **function** is a group of statements designed to perform a specific task. Functions make your code modular, reusable, and easier to debug.

### Example of a Basic Function:
```python
def my_func():
    x = "Hello World!"  # Task performed by the function
    print(x)

# Calling the function
my_func()
```

---

## **Creating a Function**
To define a function in Python:
1. Use the `def` keyword.
2. Provide a **function name**.
3. Use **round brackets `()`** followed by a **colon `:`**.
4. Write a **function body** consisting of statements.
5. Ensure all lines in the function body are **indented** consistently.

### Example:
```python
def my_func():
    x = "I love Python programming!"
    print(x)

# Calling the function
my_func()
```

### **Indentation**
- Indentation is mandatory in Python. It determines the scope of the code block.
- The function body must be indented uniformly.

**Incorrect Indentation Example (produces an error):**
```python
def my_func():
x = "I love Python programming!"  # Not indented
print(x)  # Not indented
```

---

## **Calling a Function**
To execute a function, you must **call it** by its name followed by parentheses `()`.

### Example:
```python
def greet():
    print("Hello!")

# Call the function
greet()
```

---

## **Function Parameters/Arguments**
- **Parameters**: Variables declared in the function definition.
- **Arguments**: The data passed to the function when it is called.

### Example:
```python
def hello(name):  # 'name' is the parameter
    print("Hello", name)

# Call the function with an argument
hello("John")  # Output: Hello John
```

### Multiple Parameters
You can define a function with multiple parameters and pass multiple arguments separated by commas.

### Example:
```python
def add_nums(num1, num2):
    sum = num1 + num2
    print("Sum:", sum)

# Call the function with two arguments
add_nums(4, 3)  # Output: Sum: 7
```

---

## **Default Arguments**
You can assign a **default value** to a parameter. If no argument is passed, the default value is used.

### Example:
```python
def hello(name="Paul"):
    print("Hello", name)

hello("John")  # Output: Hello John
hello()        # Output: Hello Paul (default value used)
```

---

## **Keyword Arguments**
- **Keyword arguments** allow you to specify arguments by their parameter names, ignoring the order of arguments.

### Example:
```python
def my_func(fruit1, fruit2, fruit3):
    print("I love", fruit1)
    print("I love", fruit2)
    print("I love", fruit3)

# Call the function using keyword arguments
my_func(fruit3="banana", fruit2="apples", fruit1="orange")
```

---

## **The `return` Statement**
- The `return` statement allows a function to send a value back to the caller.
- Once a `return` statement is executed, the function stops running.

### Example:
```python
def add_nums(num1, num2):
    sum = num1 + num2
    return sum  # Return the sum to the caller

result = add_nums(4, 3)  # Store the returned value
print("Result:", result)  # Output: Result: 7
```

**Important!**
Any code after a `return` statement will not be executed:
```python
def add_nums(num1, num2):
    sum = num1 + num2
    return sum
    print("This line will not be executed")

print(add_nums(4, 3))
```

---

## **Exercises**
### **Exercise 1: Fix the Indentation**
Correct the indentation in the following function:
```python
def my_func():
msg = "Hello World!"
print(msg)
my_func()
```

**Solution:**
```python
def my_func():
  msg = "Hello World!"
  print(msg)

my_func()
```

---

### **Exercise 2: Add Two Numbers**
Create a function called `add_numbers` that takes two parameters, adds them, and returns the result.

**Solution:**
```python
def add_numbers(x, y):
    result = x + y
    return result

# Call the function and print the result
print(add_numbers(4, 3))  # Output: 7
```

---

## **Summary**
- **Functions** group related tasks into reusable units.
- Functions can have **parameters** for input and can use the `return` statement to send results back.
- Indentation is critical in Python; be consistent.
- Functions can have **default arguments** and use **keyword arguments** to improve flexibility.

This guide covered examples from basic function creation to advanced concepts like parameters, default values, and return statements.

---

🎉 CONGRATULATIONS ! 🎉

[week 3 >>](./../Week-3/OOP.md)
