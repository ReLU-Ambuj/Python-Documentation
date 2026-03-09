# ASCII and Unicode

## The Built-ins
- `ord(char)`: Returns the integer representing the Unicode character.
  - `ord('a') == 97`
  - `ord('A') == 65`
  - `ord('0') == 48`
- `chr(int)`: Returns a string representation of the given Unicode integer.
  - `chr(97) == 'a'`

## Common Patterns
### Finding relative position in alphabet
```python
# 'c' -> 2
index = ord('c') - ord('a')
```

### Character Frequency Array (Alphabet only)
Instead of using a hash map, we can use an array of size 26 for lowercase English letters. This is $O(1)$ space and extremely fast.

```python
freq = [0] * 26
for char in s:
    freq[ord(char) - ord('a')] += 1
```
