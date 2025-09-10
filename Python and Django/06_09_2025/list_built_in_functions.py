"""
Python List Built-in Functions
Author: Sridhar Goudu
Description: Examples and usage of various Python list built-in functions, including less commonly discussed ones like any(), all(), enumerate(), reversed(), etc.
"""

# 1. any(iterable)
# Returns True if at least one element in the iterable is True
lst = [0, 0, 3, 0]
print("any(lst):", any(lst))  # True, because 3 is considered True

# 2. all(iterable)
# Returns True if all elements in the iterable are True
lst = [1, 2, 3, 4]
print("all(lst):", all(lst))  # True
lst2 = [1, 0, 3]
print("all(lst2):", all(lst2))  # False, because 0 is False

# 3. enumerate(iterable, start=0)
# Returns index and value pairs
lst = ["a", "b", "c"]
for index, value in enumerate(lst):
    print(f"enumerate -> index: {index}, value: {value}")

# 4. reversed(seq)
# Returns an iterator that yields elements in reverse order
lst = [1, 2, 3]
for i in reversed(lst):
    print("reversed:", i)
# Convert reversed iterator to list
print("reversed as list:", list(reversed(lst)))

# 5. sorted(iterable, key=None, reverse=False)
# Returns a new sorted list
lst = [3, 1, 2]
print("sorted(lst):", sorted(lst))
print("sorted(lst, reverse=True):", sorted(lst, reverse=True))

# 6. min(iterable)
lst = [5, 3, 9]
print("min(lst):", min(lst))  # 3

# 7. max(iterable)
print("max(lst):", max(lst))  # 9

# 8. sum(iterable, start=0)
lst = [1, 2, 3]
print("sum(lst):", sum(lst))         # 6
print("sum(lst, 10):", sum(lst, 10)) # 16, starts from 10

# 9. zip(*iterables)
a = [1, 2, 3]
b = ["a", "b", "c"]
zipped = list(zip(a, b))
print("zip(a, b):", zipped)  # [(1, 'a'), (2, 'b'), (3, 'c')]

# 10. filter(function, iterable)
lst = [1, 2, 3, 4]
even = list(filter(lambda x: x % 2 == 0, lst))
print("filter even numbers:", even)  # [2, 4]

# 11. map(function, iterable)
lst = [1, 2, 3]
squared = list(map(lambda x: x**2, lst))
print("squared using map:", squared)  # [1, 4, 9]

# 12. slice()
lst = [10, 20, 30, 40, 50]
s = slice(1, 4)  # Extract elements from index 1 to 3
print("slice lst[1:4]:", lst[s])  # [20, 30, 40]

# 13. list.copy()
lst = [1, 2, 3]
lst2 = lst.copy()
print("copy of list:", lst2)  # [1, 2, 3]

# 14. list.count(value)
lst = [1, 2, 2, 3]
print("count of 2:", lst.count(2))  # 2

# 15. list.index(value, start=0, end=len(lst))
lst = [1, 2, 2, 3]
print("index of 2:", lst.index(2))  # 1

# Bonus: Using any() and all() with conditions
lst = [2, 4, 6, 8]
print("any even > 5:", any(x > 5 for x in lst))  # True
arr = [x%2 == 0 for x in lst] # comprehensive return true or false based on condition
[True, True, True, True]
print("all even:", all(x % 2 == 0 for x in lst))  # True

# Bonus: Demonstrating reversed with strings and tuples
s = "hello"
print("reversed string:", ''.join(reversed(s)))  # 'olleh'
t = (1, 2, 3)
print("reversed tuple:", tuple(reversed(t)))     # (3, 2, 1)

# Bonus: Demonstrating enumerate with start index
lst = ["x", "y", "z"]
for i, val in enumerate(lst, start=1):
    print(f"enumerate starting from 1 -> index: {i}, value: {val}")
