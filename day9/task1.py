def parseData(data):
    id = 0
    parsed = []
    for index, item in enumerate(data):
        item = int(item)
        if index % 2 == 0:
            for _ in range(item):
                parsed.append(id)
            id += 1
        else:
            for _ in range(item):
                parsed.append('.')
    return parsed

def moveLeft(data):
    newPos = data.copy()
    freePos = [x[0] for x in enumerate(data) if x[1] == '.']
    numOfNumbers = len(data) - len(freePos)
    for i in range(len(data) - 1, 0, -1):
        if newPos[i] != '.':
            newPos[freePos[0]] = newPos[i]
            freePos.pop(0)
            if len(freePos) == 0:
                break
    return newPos[:numOfNumbers]

def getChecksum(data):
    return sum(index * int(item) for index, item in enumerate(data))

with open('input.csv', 'r') as file:
    data = file.read()
    data = parseData(data)
    movedData = moveLeft(data)
    print(f'Move left: {movedData}')
    print(f'Checksum: {getChecksum(movedData)}')