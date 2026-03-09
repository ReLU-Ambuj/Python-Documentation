# Hash Map Internals (CPython)

## CPython implementation details
Since Python 3.6, dictionaries maintain their insertion order.
- To achieve this and save memory, Python uses a sparse table of indices, which points to a dense array storing actual key-value pairs.

## Performance
- **Insert**: O(1) average.
- **Lookup**: O(1) average.
- **Delete**: O(1) average.
- Space complexity: High overhead compared to lists but justified by O(1) lookups.
