# Drill 2: Contains Duplicate
# Return True if any value appears at least twice.

def contains_duplicate(nums):
    # Method 1: Set comparison
    # return len(set(nums)) != len(nums)
    
    # Method 2: Early exit (better if duplicate is early)
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

if __name__ == "__main__":
    print(contains_duplicate([1,2,3,1])) # Expected: True
