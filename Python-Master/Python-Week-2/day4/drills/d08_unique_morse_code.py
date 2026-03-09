# Drill 8: Unique Morse Code Words

def unique_morse_representations(words):
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
             "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
             "..-","...-",".--","-..-","-.--","--.."]
             
    seen = set()
    
    for word in words:
        transformation = "".join(morse[ord(c) - ord('a')] for c in word)
        seen.add(transformation)
        
    return len(seen)

if __name__ == "__main__":
    print(unique_morse_representations(["gin","zen","gig","msg"])) # Expected: 2
