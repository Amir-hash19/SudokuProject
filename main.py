import random

def print_board(board):
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("-" * 21)
        for col in range(len(board[0])):
            if col % 3 == 0 and col != 0:
                print("|", end=" ")
            if board[row][col] == 0:
                print(".", end=" ")
            else:
                print(board[row][col], end=" ")
        print()

def find_space(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def valid_move(board, num, pos):
    row, col = pos
    # چک می‌کنیم که خانه مورد نظر خالی باشد
    if board[row][col] != 0:
        print(f"Cannot overwrite the number at position ({row + 1}, {col + 1})")
        return False
    
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(len(board))]:
        return False
    box_x, box_y = col // 3 * 3, row // 3 * 3
    for i in range(box_y, box_y + 3):
        for j in range(box_x, box_x + 3):
            if board[i][j] == num:
                return False
    return True


