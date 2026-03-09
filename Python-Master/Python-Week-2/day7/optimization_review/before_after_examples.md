# Optimization: Before & After

## 1. String Concatenation
**Before (O(N^2))**
```python
s = ""
for char in word_list:
    s += char
```

**After (O(N))**
```python
s = "".join(word_list)
```

## 2. Membership Testing
**Before (O(N) per lookup)**
```python
valid_words = ["apple", "banana", "cherry"] # List
if "apple" in valid_words:
    print("Found")
```

**After (O(1) per lookup)**
```python
valid_words = {"apple", "banana", "cherry"} # Set
if "apple" in valid_words:
    print("Found")
```

## 3. Counting Frequencies
**Before (Manual loops and if statements)**
```python
counts = {}
for c in s:
    if c in counts:
        counts[c] += 1
    else:
        counts[c] = 1
```

**After (Using collections or get)**
```python
from collections import Counter
counts = Counter(s)
# OR
counts = {}
for c in s:
    counts[c] = counts.get(c, 0) + 1
```
