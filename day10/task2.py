def parse(data):
    matrix = []
    for row in range(0, len(data)):
        r = [] 
        for col in range(0, len(data[row])):
            r.append(int(data[row][col]))
        matrix.append(r)
    return matrix

def check_neighbours(matrix, row, col):
    neighbours = []
    # Define the potential moves for non-diagonal neighbors (up, down, left, right)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for move in moves:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
            neighbours.append((new_row, new_col))
    
    return neighbours

def walk(matrix, currentPos, visited):
    row, col = currentPos
    visited.append(currentPos)
    neighbours = check_neighbours(matrix, row, col)
    for neighbour in neighbours:
        if matrix[neighbour[0]][neighbour[1]] == matrix[row][col] + 1:
            print(f'Neighbour: {matrix[neighbour[0]][neighbour[1]]} located at {neighbour}')
            walk(matrix, (neighbour[0],neighbour[1]), visited)
    return visited

def getStartPoints(matrix):
    startigPoints = []
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            if matrix[row][col] == 0:
                startigPoints.append((row, col))
    return startigPoints

with open('test.csv', 'r') as file:
    start = 0
    end = 9
    data = file.read().split('\n')
    print(data)
    parsed = parse(data)

    startingPoints = getStartPoints(parsed) 
    print(f'StartingPoints: {startingPoints}')
    total = 0
    for point in startingPoints:
        print(f'Point: {point}')
        print('-----------------')
        w = walk(parsed, point, [])
        points = [parsed[coord[0]][coord[1]] for coord in w]
        print(f'Walk: {w}')
        print(f'Points: {points}')
        total += len([point for point in points if point == 9])
        print('-----------------')
        coordinatesNine = [coord for coord in w if parsed[coord[0]][coord[1]] == 9]
            
        print(f'Coordinates of 9: {coordinatesNine}')
    print(f'Total: {total}')    