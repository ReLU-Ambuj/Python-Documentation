# Collision Resolution

## What is a Collision?
Hash Maps use a hash function to map a key to an array index. A collision occurs when two distinct keys produce the same hash and map to the same index.

## Python's Approach: Open Addressing
Python dictionaries use **Open Addressing** with probing. If the slot at `hash(key) % table_size` is occupied by a different key, Python will generate a new pseudo-random sequence to probe for the next available slot.

## Why Should You Care?
1. **Amortized O(1)**: Lookups are O(1) on average.
2. **Worst Case O(N)**: If many collisions occur, lookup degrades to O(N).
3. **Immutability of Keys**: Keys must be immutable (strings, integers, tuples). You cannot use lists or dictionaries as keys because their hash would change if mutated.
