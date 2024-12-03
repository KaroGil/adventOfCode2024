def isNumeric(s):
    return s.isdigit() or s[0] == '.'

def parseInput(input):
    sequence = "mul("
    allowedSymbols = ['(', ')', 'm', 'u', 'l', ',']
    startIndex = -1
    parsed = []
    for i in range(0, len(input)):
        if input.startswith(sequence, i):
            startIndex = i
        if startIndex != -1:
            if input[i] == ")":
                parsed.append(input[startIndex:i+1])
                startIndex = -1
            elif (input[i] not in allowedSymbols and not isNumeric(input[i])):
                print("Invalid input", input[i])
                startIndex = -1

    return parsed


def multiply(ab):
    ab = ab[4:-1]
    a, b = ab.split(',')
    return int(a) * int(b)

with open('input.csv') as f:
    lines = f.readlines()
    total = 0
    
    for line in lines:
        print(parseInput(line))
        for i in parseInput(line):
            total += multiply(i)
    print(total)
