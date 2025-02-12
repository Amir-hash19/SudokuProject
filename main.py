import random # برای انجام عملیات های تصادفی استفاده میشه

def print_board(board):#با این تابعه جدول و فرم سودوکو را میسازیم
    for row in range(len(board)):#حالا با یه حلقه پیمایش میکنیم
        if row % 3 == 0 and row != 0:#هر سطر یه خط افقی چاپ میکند
            print("-" * 21)
        for col in range(len(board[0])):#این حلقه ستون های حدول رو طی میکنه
            if col % 3 == 0 and col != 0:#هر سه ستون یک علامت جدا کننده میگذاریم
                print("|", end=" ")
            if board[row][col] == 0:# چک میکنیم که جای عدد صفر نقطه بزاریم
                print(".", end=" ")
            else:
                print(board[row][col], end=" ")
        print()


def find_space(board):#در کل این تابعه فضا های خالی جدول رو به ما دهد
    for i in range(len(board)):#خروجی این بلاک کد مثل چک کردن شرایط بازی هستش
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None



def valid_move(board, num, pos):#برای بررسی این  که حرکت کار بر در ستون و جدول های ۳ تایی وجود دارد میتوانیم از این متد استفاده کنیم
    row, col = pos
    # چک می‌کنیم که خانه مورد نظر خالی باشد
    if board[row][col] != 0:#بررسی اینکه ایا خانه از قبل پر بوده یا نه
        print(f"Cannot overwrite the number at position ({row + 1}, {col + 1})")#نمایش پیغام به کاربر در صورت اشتباه بودن حرکت
        return False
    
    if num in board[row]:#چک میکنیم که ایا عدد در همان ردیف دحود دارد یا خیر
        return False
    if num in [board[i][col] for i in range(len(board))]:#بررسی اینکه عدد در ستون ها تکرار شده یا خیر
        return False
    box_x, box_y = col // 3 * 3, row // 3 * 3#تبدیل خانه ها به باکس های ۳ در ۳
    for i in range(box_y, box_y + 3):
        for j in range(box_x, box_x + 3):
            if board[i][j] == num:
                return False
    return True



def solver(board):#حالا باید منطق حل بازی را پیاده کنیم
    find = find_space(board)#میدیم به تابعی که از قبل نوشته ایم تا بررسی کند
    if not find:
        return True
    row, col = find
    for i in range(1, 10):
        if valid_move(board, i, (row, col)):#چک شود ایا عدد در خانه قرار میگیرد یا خیر
            board[row][col] = i
            if solver(board):
                return True
            board[row][col] = 0
    return False



def board_generator(difficulty):#این متد در واقع برای ما با توجه به نوع بازی جدول را تنظیم میکند 
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
    
    if difficulty == "easy":#با استفاده از مقایسه کردن میزان پر بودن جدول را تنظیم میکنیم
        empties = random.randint(30, 40)#اینجا دقیقا همان جایی هست که از کتابخانه رندوم استفاده شده
    elif difficulty == "medium":
        empties = random.randint(40, 50)
    else:
        empties = random.randint(50, 60)
    
    for _ in range(empties):
        x = random.randint(0, side - 1)
        y = random.randint(0, side - 1)
        board[x][y] = 0
    
    return board




def playing(board):#و حالا با این فانکشن ارتباط میان بقیه فانشکن هارا برقرار میکنیم
    while True:
        name_player = input("enter your name: ") #دریافت اسم کاربر
        print()
        print(f"Ok {name_player} lets start!")#خوش امد گویی
        print()
        print_board(board)
        print("\n")#گرفتن ورودی ها از کاربر
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



def choose_difficulty():#انتخاب سطح بازی با سه درجه بازی
    print("Choose difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    while True:
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            return "easy"
        elif choice == "2":
            return "medium"
        elif choice == "3":
            return "hard"
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")            



if __name__ == "__main__":#و در اخر فراخانی متد و ایجاد ارتباط
    difficulty = choose_difficulty()
    board_made = board_generator(difficulty)
    playing(board_made)
