# Frequency Counting Strategies

## 1. The `collections.Counter`
The fastest and most Pythonic way to count frequencies.
```python
from collections import Counter
counts = Counter(['a', 'b', 'a', 'c'])
# Counter({'a': 2, 'b': 1, 'c': 1})
```

## 2. Using `dict.get(key, default)`
When building a custom map incrementally:
```python
counts = {}
for item in arr:
    counts[item] = counts.get(item, 0) + 1
```

## 3. Using `collections.defaultdict`
Best for grouping elements into lists or sets:
```python
from collections import defaultdict
grouped = defaultdict(list)
for item in arr:
    grouped[len(item)].append(item)
```
