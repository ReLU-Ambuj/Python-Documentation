# Drill 14: Jewels and Stones using Sets

def num_jewels(jewels, stones):
    jewel_set = set(jewels)
    return sum(1 for s in stones if s in jewel_set)
