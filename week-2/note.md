# Python Lists
A **Python list** is an **ordered container** that holds items of various data types. Lists are one of the most versatile and commonly used data structures in Python.

### **Creating a List**
A list is created using **square brackets (`[]`)**. Items are placed inside the brackets, separated by **commas (`,`).**

#### **Example:**
```python
# Creating a simple list of pet names
pets = ["dog", "cat", "rabbit"]
print(pets)
```

### **Lists with Mixed Data Types**
Python lists can store elements of **different data types** within the same list.

#### **Example:**
```python
# A list with mixed data types
mixed_list = ["dog", 21, True]
print(mixed_list)
```

---

## **Accessing List Elements**
### **Indexing**
Use **indexing** to access specific elements in a list. Indexing starts from **0 for the first item**, **1 for the second**, and so on.

#### **Example:**
```python
# Accessing items by index
pets = ["dog", "cat", "rabbit"]
print(pets[0])  # Output: dog
print(pets[1])  # Output: cat
print(pets[2])  # Output: rabbit
```

### **Negative Indexing**
Negative indexing starts from **-1 for the last item**, **-2 for the second last**, and so on.

#### **Example:**
```python
# Accessing items using negative indexing
pets = ["dog", "cat", "rabbit"]
print(pets[-1])  # Output: rabbit
print(pets[-2])  # Output: cat
print(pets[-3])  # Output: dog
```

---

## **Accessing a Range of Items**
### **Range of Indexes**
Use a **colon (`:`)** to access a range of items. The range includes the **start index** but excludes the **end index**.

#### **Example:**
```python
pets = ["dog", "cat", "rabbit", "fish", "hamster"]
print(pets[1:3])  # Output: ['cat', 'rabbit']
```

#### **Shortcut:**
- **Omitting the Start Index:** Starts from the beginning of the list.
```python
print(pets[:2])  # Output: ['dog', 'cat']
```
- **Omitting the End Index:** Includes all items to the end of the list.
```python
print(pets[2:])  # Output: ['rabbit', 'fish', 'hamster']
```

---

## **Modifying Lists**
### **Adding Items**
#### **Using `append()`**
The `append()` method adds an item to the **end** of the list.

#### **Example:**
```python
pets = ["dog", "cat"]
pets.append("rabbit")
print(pets)  # Output: ['dog', 'cat', 'rabbit']
```

#### **Using `insert()`**
The `insert()` method adds an item at a **specific index**.

#### **Example:**
```python
pets = ["dog", "cat", "fish"]
pets.insert(0, "rabbit")  # Insert 'rabbit' at index 0
pets.insert(2, "hamster") # Insert 'hamster' at index 2
print(pets)  # Output: ['rabbit', 'dog', 'hamster', 'cat', 'fish']
```

---

### **Deleting Items**
#### **Using `pop()`**
The `pop()` method removes the **last item** by default or an item at a specified index.

#### **Example:**
```python
pets = ["dog", "cat", "rabbit"]
pets.pop()
print(pets)  # Output: ['dog', 'cat']
```

#### **Using `remove()`**
The `remove()` method deletes an item by **value.**

#### **Example:**
```python
pets = ["dog", "cat", "rabbit"]
pets.remove("cat")
print(pets)  # Output: ['dog', 'rabbit']
```

#### **Using `del` Keyword**
Use the `del` keyword to remove an item by **index.**

#### **Example:**
```python
pets = ["dog", "cat", "rabbit"]
del pets[1]  # Deletes 'cat'
print(pets)  # Output: ['dog', 'rabbit']
```

---

## **Other List Operations**
### **Getting the Length**
Use the `len()` method to get the **number of items** in a list.

#### **Example:**
```python
pets = ["dog", "cat", "rabbit"]
print(len(pets))  # Output: 3
```

### **Changing an Item's Value**
Access the index of the item you want to modify and use the **assignment operator (`=`)**.

#### **Example:**
```python
pets = ["dog", "cat", "rabbit"]
pets[2] = "fish"  # Change 'rabbit' to 'fish'
print(pets)  # Output: ['dog', 'cat', 'fish']
```

---

### **Checking for an Item**
Use the **`in` operator** to check if an item exists in a list.

#### **Example:**
```python
pets = ["dog", "cat", "rabbit"]
print("dog" in pets)     # Output: True
print("python" in pets)  # Output: False
```

---

### **Extending a List**
The `extend()` method combines two lists.

#### **Example:**
```python
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums1.extend(nums2)
print(nums1)  # Output: [1, 2, 3, 4, 5, 6]
```

---

### **Looping Through a List**
Use a **`for` loop** to iterate through all the items in a list.

#### **Example:**
```python
pets = ["dog", "cat", "rabbit"]
for pet in pets:
    print(pet)
```

---

## **Creating Lists**
### **Using the `list()` Constructor**
An alternative way to create a list is by using the **`list()` constructor.**

#### **Example:**
```python
pets = list(("dog", "cat", "rabbit"))  # Note the double parentheses
print(pets)  # Output: ['dog', 'cat', 'rabbit']
```

---

## **Practice Exercises**
1. **Create a list of car brands and print it.**
   ```python
   cars = ["Toyota", "Honda", "Ford"]
   print(cars)
   ```

2. **Access and print "Toyota" from the list of cars.**
   ```python
   cars = ["Toyota", "Honda", "Ford"]
   print(cars[0])  # Output: Toyota
   ```

3. **Add a new car brand to the list and print it.**
   ```python
   cars.append("BMW")
   print(cars)  # Output: ['Toyota', 'Honda', 'Ford', 'BMW']
   ```

4. **Remove "Ford" from the list and print it.**
   ```python
   cars.remove("Ford")
   print(cars)  # Output: ['Toyota', 'Honda', 'BMW']
   ```

5. **Combine two lists of numbers.**
   ```python
   nums1 = [1, 2, 3]
   nums2 = [4, 5, 6]
   nums1.extend(nums2)
   print(nums1)  # Output: [1, 2, 3, 4, 5, 6]
   ```

---

# Python Set

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

# Python Tuple

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
```