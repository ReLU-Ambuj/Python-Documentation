# Drill 10: Word Pattern

def word_pattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False
        
    char_to_word = {}
    word_to_char = {}
    
    for c, w in zip(pattern, words):
        if c in char_to_word and char_to_word[c] != w:
            return False
        if w in word_to_char and word_to_char[w] != c:
            return False
            
        char_to_word[c] = w
        word_to_char[w] = c
        
    return True

if __name__ == "__main__":
    print(word_pattern("abba", "dog cat cat dog")) # Expected: True
