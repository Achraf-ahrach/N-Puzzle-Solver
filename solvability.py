def make_goal(size):
    ts = size * size
    puzzle = [-1 for i in range(ts)]
    cur = 1
    x = 0
    ix = 1
    y = 0
    iy = 0
    while True:
        puzzle[x + y * size] = cur
        if cur == 0:
            break
        cur += 1
        if x + ix == size or x + ix < 0 or (ix != 0 and puzzle[x + ix + y * size] != -1):
            iy = ix
            ix = 0
        elif y + iy == size or y + iy < 0 or (iy != 0 and puzzle[x + (y + iy) * size] != -1):
            ix = -iy
            iy = 0
        x += ix
        y += iy
        if cur == size * size:
            cur = 0
    
    # Convert flat list to tuple of tuples
    goal_2d = tuple(tuple(puzzle[i * size:(i + 1) * size]) for i in range(size))
    return goal_2d


def get_inversion_count(arr, goal):
    """
    Count inversions relative to the goal state.
    """
    inv_count = 0
    # Flatten goal if it's 2D
    flat_goal = [val for row in goal for val in row] if isinstance(goal[0], (list, tuple)) else goal

    # Create a mapping of value to its position in goal
    goal_pos = {val: idx for idx, val in enumerate(flat_goal)}
    
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] != 0 and arr[j] != 0:
                # Compare positions in goal state
                if goal_pos[arr[i]] > goal_pos[arr[j]]:
                    inv_count += 1
    return inv_count


def is_solvable(board, size):
    # Flatten the board
    flat_board = board if isinstance(board, list) and isinstance(board[0], int) else [j for row in board for j in row]

    # Get the goal state (as tuple of tuples)
    goal = make_goal(size)

    # Count inversions relative to goal
    inv_count = get_inversion_count(flat_board, goal)
    
    # For odd-sized puzzles
    if size % 2 == 1:
        solvable = inv_count % 2 == 0
    # For even-sized puzzles
    else:
        # Find the row of the blank tile (0) from the bottom
        blank_pos = flat_board.index(0)
        blank_row_from_bottom = size - (blank_pos // size)
        
        # Puzzle is solvable if (inversions + blank row from bottom) is odd
        solvable = (inv_count + blank_row_from_bottom) % 2 == 1
    
    return solvable, goal