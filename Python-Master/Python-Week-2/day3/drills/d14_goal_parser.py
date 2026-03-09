# Drill 14: Goal Parser Interpretation

def interpret(command):
    res = []
    i = 0
    while i < len(command):
        if command[i] == 'G':
            res.append('G')
            i += 1
        elif command[i] == '(' and command[i+1] == ')':
            res.append('o')
            i += 2
        else: # '(al)'
            res.append('al')
            i += 4
    return "".join(res)

if __name__ == "__main__":
    print(interpret("G()(al)")) # Expected: "Goal"
