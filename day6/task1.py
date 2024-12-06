def getDirection(data, currentPos):
    marker = data[currentPos[1]][currentPos[0]]
    direction = ''
    if marker == '>':
        direction = 'R'
    elif marker == '<':
        direction = 'L'
    elif marker == '^':
        direction = 'U'
    elif marker == 'v':
        direction = 'D'
    return direction

direction = ''

def checkBounds(data, x, y):
    borderLeft = 0
    borderRight = len(data[0]) - 1
    borderTop = 0
    borderBottom = len(data) - 1
    if x < borderLeft or x > borderRight or y < borderTop or y > borderBottom:    
        return False
    return True

def checkMove(data, x, y):
    global direction
    if not checkBounds(data, x, y):
        return False

    print(f"Checking cell: ({x}, {y}), Value: {data[y][x]}")
    if data[y][x] == '#':
        turn()
        return False
    return True

def move(data, currentPos):
    global direction
    if direction == 'U' and checkMove(data, currentPos[0], currentPos[1] - 1):
        return (currentPos[0], currentPos[1] - 1)
    elif direction == 'D' and checkMove(data, currentPos[0], currentPos[1] + 1):
        return (currentPos[0], currentPos[1] + 1)
    elif direction == 'L' and checkMove(data, currentPos[0] - 1, currentPos[1]):
        return (currentPos[0] - 1, currentPos[1])
    elif direction == 'R' and checkMove(data, currentPos[0] + 1, currentPos[1]):
        return (currentPos[0] + 1, currentPos[1])
    else:
        print('Error in move function')
        print(currentPos, direction)
        return currentPos

def getPos(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '>' or data[i][j] == '<' or data[i][j] == '^' or data[i][j] == 'v':
                return (j, i)

def turn():
    global direction
    if direction == 'U':
        direction = 'R'
    elif direction == 'R':
        direction = 'D'
    elif direction == 'D':
        direction = 'L'
    elif direction == 'L':
        direction = 'U'

with open('input.csv', 'r') as f:
    data = f.read().split('\n')
    for i in range(len(data)):
        row = []
        for char in data[i]:
            row.append(char)
        data[i] = row
    print("shape", len(data), len(data[0]))

    for i in range(len(data)):
        for j in range(len(data[i])):
            print(data[i][j], end='')
        print()


    path = []
    currentPos = getPos(data)
    direction = getDirection(data, currentPos)
    while True:
        path.append(currentPos)

        currentPos = move(data, currentPos)

        if not checkBounds(data, currentPos[0] + 1, currentPos[1] + 1):
            break
    path.append(currentPos)
    print("Total visited", len(set(path)))


   