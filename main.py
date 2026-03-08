import sys
import argparse
from parser import parse_file
from solvability import is_solvable

def print_board(board, size):
    """Print the board in a formatted way"""
    for row in board:
        print(" ".join(str(num) for num in row))
        
def main():
    parser = argparse.ArgumentParser(description="N-Puzzle Solver")
    parser.add_argument("file", help="Path to the puzzle file")
    parser.add_argument("-f", "--function", choices=['manhattan', 'hamming', 'linear'], 
                        default='manhattan', help="Heuristic function to use")
    
    args = parser.parse_args()

    # 1. Parse
    size, board = parse_file(args.file)
    print(f"Puzzle Size: {size}x{size}")

    # 2. Check Solvability
    solvable, goal = is_solvable(board, size)
    if not solvable:
        print("This puzzle is unsolvable.")
        sys.exit(0)
        
    print("Puzzle is solvable. Starting search...")
    print("\nGoal State:")
    print_board(goal, size)
    
    # 3. TODO: Call A* Solver (solver.py)
    # results = a_star(board, size, args.h_func)

if __name__ == "__main__":
    main()