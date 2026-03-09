import sys

def parse_file(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        
        clean_lines = []
        for line in lines:
            if '#' in line:
                line = line[:line.index('#')]
            line = line.strip()
            if line:
                clean_lines.append(line)
        
        if not clean_lines:
            print("Error: Empty puzzle file")
            sys.exit(1)
        
        # First line is the size
        size = int(clean_lines[0])
        
        if size < 3:
            print("Error: Puzzle size must be at least 3")
            sys.exit(1)
        
        # Parse the board
        board = []
        for i in range(1, size + 1):
            if i >= len(clean_lines):
                print(f"Error: Not enough rows. Expected {size} rows.")
                sys.exit(1)
            
            row = list(map(int, clean_lines[i].split()))
            
            if len(row) != size:
                print(f"Error: Row {i} has {len(row)} elements, expected {size}")
                sys.exit(1)
            
            board.append(tuple(row))
        
        # Validate the numbers
        flat_board = [num for row in board for num in row]
        expected_nums = set(range(size * size))
        actual_nums = set(flat_board)
        
        if actual_nums != expected_nums:
            missing = expected_nums - actual_nums
            duplicates = [num for num in flat_board if flat_board.count(num) > 1]
            invalid = actual_nums - expected_nums
            
            if duplicates:
                print(f"Error: Duplicate numbers found: {set(duplicates)}")
            if missing:
                print(f"Error: Missing numbers: {missing}")
            if invalid:
                print(f"Error: Invalid numbers (out of range): {invalid}")
            
            print(f"Expected numbers: 0 to {size * size - 1}")
            sys.exit(1)
        
        return size, tuple(board)
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: Invalid puzzle format - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)