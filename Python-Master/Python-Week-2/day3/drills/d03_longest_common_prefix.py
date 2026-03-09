# Drill 3: Longest Common Prefix
# Find the longest common prefix string amongst an array of strings.

def longest_common_prefix(strs):
    if not strs:
        return ""
        
    for i in range(len(strs[0])):
        c = strs[0][i]
        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != c:
                return strs[0][:i]
                
    return strs[0]

if __name__ == "__main__":
    print(longest_common_prefix(["flower", "flow", "flight"])) # Expected: "fl"
