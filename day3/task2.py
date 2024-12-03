enabled = True
def isNumeric(s):
    return s.isdigit() or s[0] == '.'

def parseInput(input):
    sequences = ["mul(", "do(", "don't("]
    allowedSymbols = ['(', ')', 'm', 'u', 'l', ',', 'd', 'o', 'n', "'", 't']
    startIndex = -1
    parsed = []
    for i in range(0, len(input)):
        for seq in sequences:
            if input.startswith(seq, i):
                startIndex = i
        if startIndex != -1:
            if input[i] == ")":
                parsed.append(input[startIndex:i+1])
                startIndex = -1
            elif (input[i] not in allowedSymbols and not isNumeric(input[i])):
                startIndex = -1

    return parsed


def multiply(ab):
    global enabled
    if ab == "don't()":
        enabled = False
        return 0
    elif ab == "do()":
        enabled = True
        return 0
    if enabled:
        ab = ab[4:-1]
        a, b = ab.split(',')
        return int(a) * int(b)
    else:
        return 0

with open('input.csv') as f:
    lines = f.readlines()
    total = 0
    
    for line in lines:
        for i in parseInput(line):
            total += multiply(i)
    print(total)
