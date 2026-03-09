# Drill 2: First Negative Integer in every Window of Size K
# Type: Fixed Window + Queue

from collections import deque

def first_negative_integer(arr, k):
    neg_indices = deque()
    result = []
    
    for i in range(len(arr)):
        if arr[i] < 0:
            neg_indices.append(i)
            
        if i >= k - 1:
            if neg_indices and neg_indices[0] < i - k + 1:
                neg_indices.popleft()
                
            if neg_indices:
                result.append(arr[neg_indices[0]])
            else:
                result.append(0)
                
    return result

if __name__ == "__main__":
    print(first_negative_integer([12, -1, -7, 8, -15, 30, 16, 28], 3))
    # Expected: [-1, -1, -7, -15, -15, 0]
