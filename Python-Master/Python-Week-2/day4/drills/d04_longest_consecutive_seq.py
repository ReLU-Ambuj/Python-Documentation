# Drill 4: Longest Consecutive Sequence
# O(N) Time complexity using a Hash Set

def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    
    for num in num_set:
        # Only start counting if it is the start of a sequence
        if (num - 1) not in num_set:
            current_num = num
            current_streak = 1
            
            while (current_num + 1) in num_set:
                current_num += 1
                current_streak += 1
                
            longest = max(longest, current_streak)
            
    return longest

if __name__ == "__main__":
    print(longest_consecutive([100, 4, 200, 1, 3, 2])) # Expected: 4 (1,2,3,4)
