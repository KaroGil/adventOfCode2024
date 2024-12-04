
def check(c, i, j, data):
    if c == "A" and i > 0 and j > 0 and i < len(data) - 1 and j < len(data[0]) - 1:
        # Pattern 1
        if data[i - 1][j + 1] == "S" and data[i + 1][j + 1] == "S" and data[i - 1][j - 1] == "M" and data[i + 1][j - 1] == "M":
            return 1
        # Pattern 2
        if data[i - 1][j + 1] == "M" and data[i + 1][j + 1] == "M" and data[i - 1][j - 1] == "S" and data[i + 1][j - 1] == "S":
            return 1
        # Pattern 3
        if data[i - 1][j + 1] == "M" and data[i + 1][j + 1] == "S" and data[i - 1][j - 1] == "M" and data[i + 1][j - 1] == "S":
            return 1
        # Pattern 4
        if data[i - 1][j + 1] == "S" and data[i + 1][j + 1] == "M" and data[i - 1][j - 1] == "S" and data[i + 1][j - 1] == "M":
            return 1
    return 0    

with open('input.csv', 'r') as file:
    data = file.read().split('\n')
    total = 0

    for i in range(len(data)):
        for j in range(len(data[0])):
            c = data[i][j]
            total += check(c, i, j, data)
            

    print(total)