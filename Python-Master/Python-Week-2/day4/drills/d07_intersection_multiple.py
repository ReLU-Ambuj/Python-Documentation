# Drill 7: Intersection of Multiple Arrays

def intersection(nums):
    counts = {}
    for arr in nums:
        for val in arr:
            counts[val] = counts.get(val, 0) + 1
            
    res = []
    for val, count in counts.items():
        if count == len(nums):
            res.append(val)
            
    return sorted(res)

if __name__ == "__main__":
    print(intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]])) # Expected: [3, 4]
