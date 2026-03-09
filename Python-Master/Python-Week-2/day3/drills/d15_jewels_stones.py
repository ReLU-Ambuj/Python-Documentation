# Drill 15: Jewels and Stones

def num_jewels_in_stones(jewels, stones):
    # Use hash set for O(1) lookups
    jewel_set = set(jewels)
    
    return sum(1 for s in stones if s in jewel_set)
    # Time: O(J + S)
    # Space: O(J)

if __name__ == "__main__":
    print(num_jewels_in_stones("aA", "aAAbbbb")) # Expected: 3
