# Drill 12: Reverse Words in a String
# Multiple spaces between words should be reduced to a single space.

def reverse_words(s):
    # Pythons string split() inherently handles multiple whitespaces!
    words = s.split()
    
    # Reverse the array of words and join with single space
    return " ".join(words[::-1])

    # Manual approach without split():
    # ... requires pointer manipulation and handling trailing/leading spaces.

if __name__ == "__main__":
    print(reverse_words("  hello world  ")) # Expected: "world hello"
