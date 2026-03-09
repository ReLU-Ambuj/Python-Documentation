# Drill 15: Destination City
# Using sets for path logic

def dest_city(paths):
    outgoing = set(p[0] for p in paths)
    
    for _, dest in paths:
        if dest not in outgoing:
            return dest
            
    return ""

if __name__ == "__main__":
    print(dest_city([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
    # Expected: "Sao Paulo"
