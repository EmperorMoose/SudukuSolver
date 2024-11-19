import random

def create_empty_board():
    """Create a 9x9 grid pre-filled with example data."""
    board = [[(i * 3 + j) % 9 + 1 for j in range(9)] for i in range(9)]
    return board

def is_valid(board, row, col, num):
    if num in board[row]:
        return False

    if num in (board[i][col] for i in range(9)):
        return False

    box_row, box_col = 3 * (row // 3), 3 * (col // 3) #explain these double slashes
    for i in range (box_row, box_row + 3):
        for j in range (box_col, box_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1,10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def generate_solved_board():
    board = create_empty_board()
    numbers = list(range(1,10))
    for row in range(9):
        for col in range(9):
            random.shuffle(numbers) #shuffle?
            for num in numbers:
                if is_valid(board,row,col,num):
                    board[row][col] = num
                    break

    solve(board)
    return board

def remove_numbers(board, difficulty = 40):
    cells = [(r,c) for r in range(9) for c in range(9)]
    random.shuffle(cells)
    for _ in range (difficulty):
        row, col = cells.pop()
        board[row][col] = 0

    return board

def display_board(board):
    """Print the sudoku board as ASCII art."""
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # horizontal divider
        row_display = " | ".join(
            " ".join(str(cell) if cell != 0 else "." for cell in row[j:j+3])
            for j in range(0, 9, 3)
        )
        print(row_display)

if __name__ == "__main__":
    # Generate a solved board
    solved_board = generate_solved_board()
    print("Solved Board:")
    display_board(solved_board)

    # Create a puzzle
    puzzle_board = remove_numbers(solved_board, difficulty=40)
    print("\nPuzzle Board:")
    display_board(puzzle_board)
