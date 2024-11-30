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