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