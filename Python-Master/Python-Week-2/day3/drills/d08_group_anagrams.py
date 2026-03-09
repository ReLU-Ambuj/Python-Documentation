# Drill 8: Group Anagrams

from collections import defaultdict

def group_anagrams(strs):
    ans = defaultdict(list)
    
    for s in strs:
        # Create a frequency count of 26 zeros
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
            
        # Tuple of frequencies as key (O(K) time where K is max str len)
        ans[tuple(count)].append(s)
        
    return list(ans.values())

if __name__ == "__main__":
    print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
    # Expected: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] (order may vary)
