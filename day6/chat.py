def simulate(grid, start_pos, start_dir, obstruction=None):
    rows, cols = len(grid), len(grid[0])
    directions = ["up", "right", "down", "left"]
    move = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
    
    # Place the obstruction if provided
    if obstruction:
        grid[obstruction[0]][obstruction[1]] = "#"
    
    path = []
    x, y = start_pos
    dir_idx = directions.index(start_dir)
    steps = 0
    max_steps = rows * cols * 4  # Arbitrary large step limit to detect loops
    
    while steps < max_steps:
        state = (x, y, dir_idx)
        if state in path:
            # Check if we're stuck in a loop
            loop_start = path.index(state)
            loop = path[loop_start:]
            if len(set(loop)) < len(loop):
                # True loop detected
                if obstruction:
                    grid[obstruction[0]][obstruction[1]] = "."
                return True
        path.append(state)
        
        # Move in the current direction
        dx, dy = move[directions[dir_idx]]
        nx, ny = x + dx, y + dy
        
        # Check boundaries and obstacles
        if not (0 <= nx < rows and 0 <= ny < cols) or grid[nx][ny] == "#":
            dir_idx = (dir_idx + 1) % 4  # Turn clockwise
        else:
            x, y = nx, ny  # Move forward
        
        steps += 1
    
    # No loop detected
    if obstruction:
        grid[obstruction[0]][obstruction[1]] = "."
    return False

def find_obstruction_positions(grid, start_pos, start_dir):
    rows, cols = len(grid), len(grid[0])
    valid_positions = []
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "." and (r, c) != start_pos:
                # Test placing an obstruction at (r, c)
                if simulate([row[:] for row in grid], start_pos, start_dir, (r, c)):
                    valid_positions.append((r, c))
    
    return valid_positions

with open('test.csv', 'r') as f:
    input_map = [list(line.strip()) for line in f]


start_pos = (6, 4)  # Example starting position
start_dir = "up"  # Example starting direction

valid_positions = find_obstruction_positions(input_map, start_pos, start_dir)
print(f"Number of valid positions: {len(valid_positions)}")
print("Valid positions:", valid_positions)
