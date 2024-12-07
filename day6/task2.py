from itertools import cycle


def findObstructionPositions(data, start_pos, start_dir):
    valid_positions = []

    for i in range(len(data)):
        for j in range(len(data[i])):
            # Skip non-empty positions and the starting position
            if data[i][j] == "." and (i, j) != start_pos:
                copyData = [row[:] for row in data]  # Create a copy of the grid
                copyData = putObstruction(copyData, (i, j))

                # Use pos_counter to check for loops
                if pos_counter(copyData, start_pos, obstacle=(i, j))[1]:
                    valid_positions.append((i, j))

    print(f"Found {len(valid_positions)} valid obstruction positions.")
    return valid_positions



def pos_counter(lab, current, obstacle=(-1, -1)):
    """Navigate the grid and detect loops."""
    directions = cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])  # Reset directions
    is_loop = False
    cur_dir = next(directions)  # Start with the first direction
    visited = {(current, cur_dir)}  # Track visited positions and directions

    while True:
        # Calculate the new position
        new = tuple(a + b for a, b in zip(current, cur_dir))

        # Check bounds and obstacles
        if not ((0 <= new[1] < len(lab[0])) and (0 <= new[0] < len(lab))):
            break  # Out of bounds
        elif lab[new[0]][new[1]] == "#" or new == obstacle:
            cur_dir = next(directions)  # Turn to the next direction
        else:
            current = new  # Move to the new position

        # Check for loops
        if (current, cur_dir) in visited:
            is_loop = True
            break

        visited.add((current, cur_dir))  # Mark as visited

    return len({v0 for v0, v1 in visited}), is_loop, {v[0] for v in visited}


def getStartPosition(data):
    """Locate the starting position and direction in the grid."""
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == ">":
                return (i, j), (0, 1)  # Right
            elif data[i][j] == "<":
                return (i, j), (0, -1)  # Left
            elif data[i][j] == "^":
                return (i, j), (-1, 0)  # Up
            elif data[i][j] == "v":
                return (i, j), (1, 0)  # Down


def putObstruction(data, pos):
    """Place an obstruction (#) at the specified position."""
    data[pos[0]][pos[1]] = "#"
    print(f"Placed obstruction at position {pos}.")
    return data


def find_path(data, start_pos, start_dir):
    """Find the path and detect loops."""
    directions = cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])  # Up, Right, Down, Left
    current = start_pos
    cur_dir = start_dir
    visited = {(current, cur_dir)}

    while True:
        # Calculate the new position
        new = tuple(a + b for a, b in zip(current, cur_dir))

        # Check bounds and obstacles
        if not ((0 <= new[1] < len(data[0])) and (0 <= new[0] < len(data))):
            break  # Out of bounds
        elif data[new[0]][new[1]] == "#":
            cur_dir = next(directions)  # Turn to the next direction
        else:
            current = new  # Move to the new position

        # Check for loops
        if (current, cur_dir) in visited:
            return list(visited)  # Return the visited path

        visited.add((current, cur_dir))  # Mark as visited

    return []  # No loop detected


with open('input.csv', 'r') as file:
    data = file.read().split('\n')
    for i in range(len(data)):
        row = []
        for char in data[i]:
            row.append(char)
        data[i] = row
    print("shape", len(data), len(data[0]))

    # Find the starting position and direction
    start_pos, start_dir = getStartPosition(data)
    print("Start position and direction:", start_pos, start_dir)

    # Find all valid obstruction positions
    valid_positions = findObstructionPositions(data, start_pos, start_dir)

    # Output the results
    print("Valid obstruction positions:", valid_positions)
    print(f"Total number of obstruction positions: {len(valid_positions)}")

