
def plot_obstacles(obstacles, grid):
    for x,y in obstacles:
        x, y = int(x), int(y)
        grid[y][x] = '#'

def make_grid(width, height):
    return [['.' for _ in range(width)] for _ in range(height)]

def shortest_path(grid, start, end):
    queue = [(start, 0)]
    visited = set()
    while queue:
        (x, y), distance = queue.pop(0)
        if (x, y) == end:
            return distance
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid) and grid[new_y][new_x] != '#':
                queue.append(((new_x, new_y), distance + 1))

    return -1

with open('input.csv') as file:
    lines = file.read().splitlines()
    grid = make_grid(71,71)
    obstacles = [line.split(',') for line in lines]
    for row in grid:
        for cell in row:
            print(cell, end='')
        print()

    start = (0, 0)
    end = (70, 70)
    stop = []
    for n in range(1, len(obstacles) + 1):
        grid = make_grid(71, 71)
        plot_obstacles(obstacles[:n], grid)

        if shortest_path(grid, start, end) == -1:
            print(f'Number of obstacles: {obstacles[n]}')
            stop.append(obstacles[n - 1])
            break
        
    
    print(f'Number of obstacles: {stop}')
    print(f'Shortest path from start to end {shortest_path(grid, start, end)}')