# Time Complexity Optimization Tips

1. **Nested Loops vs Hash Maps**: The biggest leap is turning $O(N^2)$ brute force pairs into $O(N)$ lookups using a Hash Map (`Two Sum` pattern).
2. **Sorting**: If you are repeatedly finding the minimum/maximum or grouping items, consider sorting first ($O(N \log N)$) to group elements adjacently.
3. **Sliding Window**: Replace overlapping recalculations. If you need the sum of a 4-element window, don't recount 4 elements every time. Subtract the left-most element and add the new right element ($O(1)$ updates).
4. **Binary Search**: If an array/matrix is sorted, replace $O(N)$ linear scans with $O(\log N)$ binary searches.
