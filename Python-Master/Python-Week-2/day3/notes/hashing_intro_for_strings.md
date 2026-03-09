# Hashing for Strings

## Concept
Hashing allows $O(1)$ expected time complexity for lookups, insertions, and deletions. For strings, hashing is incredibly useful for grouping, counting, and pattern matching.

## Hashing Signatures
When problems ask to group strings that are "similar" (e.g. anagrams, isomorphic patterns), we need to compute a unique "signature" or "key" that can be hashed.

### Anagram Grouping Key
Since anagrams have the exact same character frequencies, a sorted version of the string OR a frequency tuple can serve as a key.
- Key = `tuple(freq_array)` (O(N) generation)
- Key = `"".join(sorted(s))` (O(N log N) generation)

### Isomorphic Pattern Key
When checking if structural patterns match, map characters to their first seen index or map them bi-directionally between two strings.
