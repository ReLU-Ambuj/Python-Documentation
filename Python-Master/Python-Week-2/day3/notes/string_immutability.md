# String Immutability

## What does immutable mean?
In Python, once a string is created in memory, it cannot be changed. Any operation that appears to modify a string (like `.replace()`, `.upper()`, or concatenation `+`) actually creates a **new string object** in memory.

## The Problem with `+=` in Loops
```python
# BAD! O(N^2) complexity because a new string is created each iteration.
s = ""
for char in large_string:
    s += char 
```

## The Solution: `.join()`
When dynamically building large strings, use a list to collect characters/substrings, then join them at the end. This is $O(N)$.
```python
# GOOD! O(N) complexity.
char_list = []
for char in large_string:
    char_list.append(char)
s = "".join(char_list)
```

## When to use what
- String matching / Searching (`in`, `.find()`, `.startswith()`) is highly optimized in Python.
- For heavy mutation, convert string to `list(s)`, mutate the list, and `"".join(L)` at the end.
