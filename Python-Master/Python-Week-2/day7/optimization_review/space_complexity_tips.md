# Space Complexity Optimization Tips

1. **In-place modifications**: If a problem allows mutating the input array (like `Rotate Image` or `Reverse String`), do it! It reduces space from `O(N)` to `O(1)`.
2. **Re-use arrays**: If returning a list of the same size, can you overwrite the input list instead?
3. **Avoid creating unnecessary slices**: `arr[::-1]` creates a full copy of the array in memory. If you only need to iterate backwards, use `range(len(arr)-1, -1, -1)`.
4. **Use Generators/Iterators**: When calculating sums or chains, use `sum(len(x) for x in arr)` instead of `sum([len(x) for x in arr])` (no brackets = generator = O(1) space).
