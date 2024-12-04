word = "XMAS"
def checkLine(line):
    count = 0
    start = 0
    while True:
        start = line.find(word, start)
        if start == -1:
            break
        count += 1
        start += 1
    return count

def makeVerticalLine(data, j):
    verticalLine = ""
    for i in range(len(data)):
        verticalLine += data[i][j]
    return verticalLine

def makeDiagonalLine(data, i, j, direction="leftToRight"):
    diagonalLine = ""
    rows, cols = len(data), len(data[0])

    while 0 <= i < rows and 0 <= j < cols:
        diagonalLine += data[i][j]
        if direction == "leftToRight":
            i += 1
            j += 1
        elif direction == "rightToLeft":
            i += 1
            j -= 1
    
    return diagonalLine


def reverseLine(line):
    return line[::-1]

with open('input.csv', 'r') as file:
    data = file.read().split('\n')
    total = 0
    for line in data:
        total+= checkLine(line)
        total += checkLine(reverseLine(line))
    for i in range(len(data[0])):
        verticalLine = makeVerticalLine(data, i)
        total += checkLine(verticalLine)
        total += checkLine(reverseLine(verticalLine))
    for i in range(len(data)):
        for j in range(len(data[0])):
            if i == 0 or j == 0: 
                diagonalLine = makeDiagonalLine(data, i, j, "leftToRight")
                total += checkLine(diagonalLine)
                total += checkLine(reverseLine(diagonalLine))
            
            if i == 0 or j == len(data[0]) - 1: 
                diagonalLine = makeDiagonalLine(data, i, j, "rightToLeft")
                total += checkLine(diagonalLine)
                total += checkLine(reverseLine(diagonalLine))

    print(total)