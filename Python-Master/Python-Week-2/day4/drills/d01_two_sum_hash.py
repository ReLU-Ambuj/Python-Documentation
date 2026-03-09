# Drill 1: Two Sum (Hash Map O(N))
# Return indices of the two numbers such that they add up to target.

def two_sum(nums, target):
    # num -> index
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
        
    return []

if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9)) # Expected: [0, 1]
