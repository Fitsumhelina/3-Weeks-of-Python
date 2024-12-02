

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

---


# 02 Python Set

## **Introduction to Sets**
A **set** in Python is an **unordered collection of unique items**. Sets are commonly used for storing unique elements, performing set operations, and removing duplicates.

### **Key Characteristics**
- **Unordered**: Items do not have a fixed position or order.
- **Mutable**: You can add or remove items, but the individual items must be immutable (e.g., strings, numbers, tuples).
- **Unique**: Duplicate items are automatically removed.
  
---

## **Creating a Set**
You can create a set using curly brackets `{}` or the `set()` constructor.

### **Examples**
```python
# Using curly brackets
fruits = {"apple", "banana", "cherry"}
print(fruits)  # Output: {'apple', 'banana', 'cherry'}

# Using the set() constructor
colors = set(["red", "blue", "green"])
print(colors)  # Output: {'red', 'blue', 'green'}
```

### **Note**
Sets cannot contain mutable types like lists, dictionaries, or other sets. They can, however, include immutable types like strings, numbers, and tuples.

---

## **Accessing Items**
Since sets are unordered, they do not support indexing or slicing. However, you can loop through a set.

### **Example**
```python
pets = {"dog", "cat", "rabbit"}
for pet in pets:
    print(pet)
# Output (order may vary):
# dog
# cat
# rabbit
```

---

## **Adding Items to a Set**
You can add elements to a set using:
1. **`add()`**: Adds a single item.
2. **`update()`**: Adds multiple items or merges another iterable.

### **Examples**
```python
# Adding a single item
pets = {"dog", "cat"}
pets.add("rabbit")
print(pets)  # Output: {'dog', 'cat', 'rabbit'}

# Adding multiple items
pets.update(["parrot", "fish"])
print(pets)  # Output: {'dog', 'cat', 'rabbit', 'parrot', 'fish'}
```

---

## **Removing Items**
Sets allow the removal of elements using:
1. **`remove()`**: Removes an item; raises an error if the item is not found.
2. **`discard()`**: Removes an item; does not raise an error if the item is not found.
3. **`pop()`**: Removes and returns a random item.
4. **`clear()`**: Removes all items from the set.

### **Examples**
```python
pets = {"dog", "cat", "rabbit"}

# Using remove()
pets.remove("cat")
print(pets)  # Output: {'dog', 'rabbit'}

# Using discard()
pets.discard("rabbit")
print(pets)  # Output: {'dog'}

# Using pop()
pets.pop()  # Removes a random item
print(pets)  # Output: {}

# Clearing the set
pets = {"dog", "cat"}
pets.clear()
print(pets)  # Output: set()
```

---

## **Set Operations**
Sets support various operations for combining, comparing, and modifying sets.

### **Union**
Combines two sets, removing duplicates. Use the `union()` method or the `|` operator.
```python
x = {1, 2, 3}
y = {3, 4, 5}
print(x.union(y))  # Output: {1, 2, 3, 4, 5}
```

### **Intersection**
Finds common items between two sets. Use the `intersection()` method or the `&` operator.
```python
print(x.intersection(y))  # Output: {3}
```

### **Difference**
Finds items in one set but not in the other. Use the `difference()` method or the `-` operator.
```python
print(x.difference(y))  # Output: {1, 2}
```

### **Symmetric Difference**
Finds items that are in either set but not in both. Use the `symmetric_difference()` method or the `^` operator.
```python
print(x.symmetric_difference(y))  # Output: {1, 2, 4, 5}
```

---

## **Other Useful Methods**
- **`issubset()`**: Checks if one set is a subset of another.
- **`issuperset()`**: Checks if one set contains another.
- **`isdisjoint()`**: Checks if two sets have no items in common.

---

## **Checking for Membership**
Use the `in` and `not in` operators to check if an item exists in a set.
```python
fruits = {"apple", "banana", "cherry"}
print("apple" in fruits)  # Output: True
print("kiwi" not in fruits)  # Output: True
```

---

## **Set Length**
Use the `len()` function to get the number of items in a set.
```python
fruits = {"apple", "banana", "cherry"}
print(len(fruits))  # Output: 3
```

---

## **Exercises**

### **Easy Exercises**
1. Create a set of five vegetables and print it.
2. Add `"mango"` to the set `{"apple", "banana", "cherry"}`.
3. Use a loop to print each item in the set `{"python", "java", "c++"}`.
4. Remove `"dog"` from the set `{"dog", "cat", "rabbit"}`.
5. Check if `"cat"` is in the set `{"dog", "cat", "rabbit"}`.

---

### **Medium Exercises**
1. Combine the sets `{1, 2, 3}` and `{3, 4, 5}` using `union()`.
2. Find the intersection of `{1, 2, 3, 4}` and `{3, 4, 5, 6}`.
3. Use the `difference()` method to find items in `{1, 2, 3, 4}` but not in `{3, 4, 5, 6}`.
4. Create a set of numbers from 1 to 5 and remove all items using `clear()`.
5. Write a program to find duplicates in a list using a set.

---

### **Hard Exercises**
1. Use a set to remove duplicate characters from a string.
   - Input: `"hello"`
   - Output: `{'h', 'e', 'l', 'o'}`
2. Create two sets of student names and find the symmetric difference.
3. Check if the set `{1, 2}` is a subset of `{1, 2, 3}`.
4. Write a function that takes two sets and returns a new set with all unique elements from both sets.
5. Create a program that counts the unique words in a sentence using a set.

---


# 03 Python Tuple

Tuples in Python are ordered, immutable containers that can hold a collection of items. Tuples are similar to lists but differ in their immutability, meaning their items cannot be modified after creation. This feature makes tuples an excellent choice for storing fixed data that shouldn't change.

---

### **Key Characteristics of Tuples**
1. **Ordered**: The items in a tuple have a defined order.
2. **Immutable**: Once created, you cannot change, add, or remove items.
3. **Supports Mixed Data Types**: Tuples can hold elements of different data types (e.g., strings, integers, booleans).

---

### **Creating a Tuple**
Tuples are created using **round brackets** `()`. Items are separated by commas.

#### Example:
```python
pets = ("dog", "cat", "rabbit")
print(pets)  # Output: ('dog', 'cat', 'rabbit')
```

#### Mixed Data Types:
```python
mixed = ("dog", 21, True)
print(mixed)  # Output: ('dog', 21, True)
```

#### Using the `tuple()` Constructor:
```python
pets = tuple(("dog", "cat", "rabbit"))  # Note the double parentheses
print(pets)  # Output: ('dog', 'cat', 'rabbit')
```

---

### **Accessing Tuple Items**
Tuples support various ways to access their elements using **indexing**, **negative indexing**, and **slicing**.

#### Indexing:
```python
pets = ("dog", "cat", "rabbit")
print(pets[0])  # Output: 'dog'
print(pets[2])  # Output: 'rabbit'
```

#### Negative Indexing:
```python
print(pets[-1])  # Output: 'rabbit' (last item)
print(pets[-2])  # Output: 'cat'
```

#### Slicing:
- Use a colon `:` to specify a range.
- The start index is inclusive, while the end index is exclusive.

```python
pets = ("dog", "cat", "rabbit", "fish", "hamster")
print(pets[1:4])  # Output: ('cat', 'rabbit', 'fish')
```

#### Omitting Start or End Index:
```python
print(pets[:3])  # Output: ('dog', 'cat', 'rabbit')
print(pets[2:])  # Output: ('rabbit', 'fish', 'hamster')
```

---

### **Tuple Operations**

#### Getting the Length:
Use the `len()` function to determine the number of items in a tuple.
```python
print(len(pets))  # Output: 5
```

#### Looping Through a Tuple:
```python
for pet in pets:
    print(pet)
# Output:
# dog
# cat
# rabbit
# fish
# hamster
```

#### Checking Membership:
Use the `in` operator to check if an item exists in the tuple.
```python
print("cat" in pets)  # Output: True
print("lion" in pets)  # Output: False
```

#### Combining Tuples:
You can combine two tuples using the `+` operator.
```python
pets1 = ("dog", "cat")
pets2 = ("rabbit", "fish")
all_pets = pets1 + pets2
print(all_pets)  # Output: ('dog', 'cat', 'rabbit', 'fish')
```

---

### **Immutability of Tuples**
Since tuples are immutable:
1. **Items cannot be changed**:
    ```python
    my_tuple = (1, 2, 3)
    my_tuple[0] = 10  # Raises an error
    ```
2. **Items cannot be added or removed**:
    ```python
    my_tuple.append(4)  # Raises an error
    my_tuple.remove(2)  # Raises an error
    ```

---

### **Tuple Exercises**

#### **Easy Exercises**
1. Create a tuple of five colors and print it.
2. Access the second and last item of a tuple.
3. Slice the tuple `("red", "blue", "green", "yellow", "purple")` to get the middle three items.
4. Check if `"orange"` exists in the tuple `("red", "blue", "green")`.
5. Use a loop to print all items in the tuple `("apple", "banana", "cherry")`.

#### **Medium Exercises**
1. Create two tuples and merge them into one.
2. Write a program to count how many times a specific item appears in a tuple.
3. Extract only the numeric items from a tuple `("apple", 42, 3.14, "banana", 7)`.
4. Find the length of the tuple `("a", "b", "c", "d", "e")` without using `len()`.
5. Use negative indexing to reverse a tuple.

#### **Hard Exercises**
1. Write a function to check if two tuples have at least one common item.
2. Convert a tuple of strings to uppercase: `("hello", "world") → ("HELLO", "WORLD")`.
3. Write a program to find the unique elements in two tuples.
4. Implement a function that takes a tuple and returns a new tuple with only even numbers.
5. Create a tuple of mixed data types and filter out only the string elements.

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
