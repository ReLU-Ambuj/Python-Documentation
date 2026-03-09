# Drill 10: Happy Number
# Cycle detection using a Hash Set

def is_happy(n):
    def get_next(number):
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit ** 2
        return total_sum

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
        
    return n == 1

if __name__ == "__main__":
    print(is_happy(19)) # Expected: True
