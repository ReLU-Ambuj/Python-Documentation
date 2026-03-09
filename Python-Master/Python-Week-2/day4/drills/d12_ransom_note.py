# Drill 12: Ransom Note

from collections import Counter

def can_construct(ransomNote, magazine):
    mag_counts = Counter(magazine)
    
    for char in ransomNote:
        if mag_counts[char] <= 0:
            return False
        mag_counts[char] -= 1
        
    return True

if __name__ == "__main__":
    print(can_construct("aa", "aab")) # Expected: True
