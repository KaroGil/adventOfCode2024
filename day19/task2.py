def checkDesign(available, design):
    n = len(design)
    dp = [0 for _ in range(n + 1)]
    # Base case
    dp[0] = 1

    # Recurrsion 
    for i in range(1, n + 1):
        for part in available:
            if design[i-len(part):i] == part:
                dp[i] += dp[i-len(part)]
    return dp[-1]

with open('input.csv', 'r') as file:
    data = file.read().splitlines()
    # Parse data from file
    available = data[0].split(', ')
    designs = data[2:]
    available.sort(key=len, reverse=True)
    print(f'Sorted list: {available}')

print(f'Possible designs: {sum(checkDesign(available, design) for design in designs)}')