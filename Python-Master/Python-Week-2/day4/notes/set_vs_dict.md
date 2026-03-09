# Set vs Dictionary

## When to use Sets (`set()`)
Use sets when you **only** care about existence / uniqueness.
- Finding duplicates.
- Finding intersections, unions, differences between collections.
- Extremely fast O(1) lookup.

## When to use Dictionaries (`dict() / {}`)
Use dictionaries when you need to map a key to *some extra state/information*.
- Counting frequencies (State = count).
- Quick index lookups (State = index in array).
- Caching / Memoization (State = computed result).
