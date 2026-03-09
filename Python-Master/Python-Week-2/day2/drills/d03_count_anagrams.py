# Drill 3: Count Occurrences of Anagrams
# Type: Fixed Window + Hash Map

from collections import Counter

def count_anagrams(text, word):
    k = len(word)
    word_count = Counter(word)
    window_count = Counter(text[:k-1]) # initialize with 1 less element
    anagrams = 0
    
    for i in range(k - 1, len(text)):
        window_count[text[i]] += 1
        
        if window_count == word_count:
            anagrams += 1
            
        # Slide window
        left_char = text[i - k + 1]
        window_count[left_char] -= 1
        if window_count[left_char] == 0:
            del window_count[left_char]
            
    return anagrams

if __name__ == "__main__":
    print(count_anagrams("forxxorfxdofr", "for")) # Expected: 3
