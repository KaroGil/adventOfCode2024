

def checkDesign(available, design):
    n = len(design)
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    for i in range(1, n + 1):
        for part in available:
            if i >= len(part) and design[i-len(part):i] == part:
                dp[i] = dp[i] or dp[i-len(part)]
    return dp[-1]

with open('test.csv', 'r') as file:
    data = file.read().splitlines()
    # Parse data from file
    available = data[0].split(', ')
    designs = data[2:]
    available.sort(key=len, reverse=True)
    print(f'Sorted list: {available}')
    possible = []
    for design in designs:
        print(f'Checking design: {design}')
        if checkDesign(available, design):
            print(design)
            possible.append(design)

print(f'Possible designs: {len(possible)}')
print(f'Possible designs: {sum(checkDesign(available, design) for design in designs)}')