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



def solver(board):
    find = find_space(board)
    if not find:
        return True
    row, col = find
    for i in range(1, 10):
        if valid_move(board, i, (row, col)):
            board[row][col] = i
            if solver(board):
                return True
            board[row][col] = 0
    return False



def board_generator(difficulty):
    base = 3
    side = base * base
    
    def pattern(r, c):
        return (base * (r % base) + r // base + c) % side
    
    def mix_operation(s):
        return random.sample(s, len(s))
    
    rbase = range(base)
    rows = [g * base + r for g in mix_operation(rbase) for r in mix_operation(rbase)]
    cols = [g * base + c for g in mix_operation(rbase) for c in mix_operation(rbase)]
    nums = mix_operation(range(1, base * base + 1))
    
    board = [[nums[pattern(r, c)] for c in cols] for r in rows]
    
    if difficulty == "easy":
        empties = random.randint(30, 40)
    elif difficulty == "medium":
        empties = random.randint(40, 50)
    else:
        empties = random.randint(50, 60)
    
    for _ in range(empties):
        x = random.randint(0, side - 1)
        y = random.randint(0, side - 1)
        board[x][y] = 0
    
    return board

def playing(board):
    while True:
        print_board(board)
        print("\n")
        row = int(input("Enter the row number (1-9): ")) - 1
        col = int(input("Enter the column number (1-9): ")) - 1
        num = int(input("Enter the number you want to put (1-9): "))
        print()
        
        if valid_move(board, num, (row, col)):
            board[row][col] = num
            if not find_space(board):
                print("Great, your puzzle is solved!")
                break
        else:
            print("Wrong move! Try again!")