# Drill 9: Subarray Product Less Than K
# Type: Variable Window (Counting combinations)

def num_subarray_product_less_than_k(nums, k):
    if k <= 1:
        return 0
        
    prod = 1
    ans = left = 0
    
    for right, val in enumerate(nums):
        prod *= val
        while prod >= k:
            prod /= nums[left]
            left += 1
        ans += right - left + 1
        
    return ans

if __name__ == "__main__":
    print(num_subarray_product_less_than_k([10, 5, 2, 6], 100)) # Expected: 8
