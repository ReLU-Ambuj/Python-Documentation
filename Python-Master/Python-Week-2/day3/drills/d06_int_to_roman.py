# Drill 6: Integer to Roman

def int_to_roman(num):
    values = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    res = []
    for val, sym in values:
        if num == 0:
            break
        count, num = divmod(num, val)
        res.append(sym * count)
        
    return "".join(res)

if __name__ == "__main__":
    print(int_to_roman(1994)) # Expected: MCMXCIV
