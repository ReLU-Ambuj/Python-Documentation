# Drill 9: Isomorphic Strings

def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
        
    map_s_t = {}
    map_t_s = {}
    
    for c1, c2 in zip(s, t):
        if (c1 in map_s_t and map_s_t[c1] != c2) or \
           (c2 in map_t_s and map_t_s[c2] != c1):
            return False
            
        map_s_t[c1] = c2
        map_t_s[c2] = c1
        
    return True

if __name__ == "__main__":
    print(is_isomorphic("egg", "add")) # Expected: True
    print(is_isomorphic("foo", "bar")) # Expected: False
