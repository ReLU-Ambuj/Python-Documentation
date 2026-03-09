# Hashing Code Review Checklist

When writing hash map/set solutions, ask yourself:

1. **Can `dict.get(key, 0)` replace your `if-else` setup checks?**
2. **Are you trying to cache mutable objects (lists/dicts)?** Use tuples instead.
3. **Can `collections.Counter` do the heavy lifting for you?**
4. **If order doesn't matter, did you use `set()` instead of `list` for membership testing?** (`in` is O(1) for sets, O(N) for lists).
5. **For alphabet-only problems, is a size-26 integer array faster and lower overhead than a full Hash Map?**
