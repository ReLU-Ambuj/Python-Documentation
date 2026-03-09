# Drill 7: Find the Index of the First Occurrence in a String (strStr)

def strStr(haystack, needle):
    # Built-in is optimized C code, but manual window is good practice
    # return haystack.find(needle)
    
    if not needle:
        return 0
        
    n_len = len(needle)
    for i in range(len(haystack) - n_len + 1):
        if haystack[i:i+n_len] == needle:
            return i
            
    return -1

if __name__ == "__main__":
    print(strStr("sadbutsad", "sad")) # Expected: 0
