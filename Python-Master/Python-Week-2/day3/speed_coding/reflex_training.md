# Reflex Training (Strings)

Strings require fast, muscular memory to navigate. Set a timer and code the following snippets iteratively until they are typed flawlessly under 2 minutes collectively.

1. **Reverse a String Iteratively (No `[::-1]`)**
   ```python
   res = []
   for i in range(len(s)-1, -1, -1):
       res.append(s[i])
   return "".join(res)
   ```

2. **Count Frequencies with an Array**
   ```python
   freq = [0] * 26
   for c in s:
       freq[ord(c) - ord('a')] += 1
   ```

3. **Check for Alphanumeric**
   ```python
   # using ord
   def is_alnum(c):
       return (ord('A') <= ord(c) <= ord('Z') or
               ord('a') <= ord(c) <= ord('z') or
               ord('0') <= ord(c) <= ord('9'))
   ```
