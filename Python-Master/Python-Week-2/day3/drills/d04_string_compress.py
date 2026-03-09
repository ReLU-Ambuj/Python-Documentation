# Drill 4: String Compression
# Compress string in-place: ["a","a","b","b","c","c","c"] -> ["a","2","b","2","c","3"]

def compress(chars):
    write = 0
    read = 0
    
    while read < len(chars):
        char = chars[read]
        count = 0
        
        while read < len(chars) and chars[read] == char:
            read += 1
            count += 1
            
        chars[write] = char
        write += 1
        
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1
                
    return write

if __name__ == "__main__":
    arr = ["a","a","b","b","c","c","c"]
    length = compress(arr)
    print(arr[:length]) # Expected: ['a', '2', 'b', '2', 'c', '3']
