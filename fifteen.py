def print_greeting():
    print("*" * 5, "Hello", "*" * 5)



def initialize_bord():
    """

    :return: list --> [15,14, ...., 3,1,2,0]
    """
    return []


def check(board):
    """

    :param bord: [1, 2, 3,...., 14, 15, 0] --> False otherwise True
    :return: True -- bord is not sorted
            False -- bord is sorted
    """
    win = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, "_"]
    if board == win:
        print("Ви виграли")
        return False
    return True


def print_bord():
    a = 0
    board = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 1, 2, "_"]
    for i in board:
        print(i, end="\t")
        a += 1
        if a == 4:
            print()
            print("_______________")
            a = 0
    return board


def move(board, moved):
    k = board.index(moved)
    n = board.index("_")
    a=0
    if n - 1 == k:
        m = board[n]
        board[n] = board[k]
        board[k] = m
        print(f"Число {moved} переміщено")

    elif n + 1 == k:
        m = board[n]
        board[n] = board[k]
        board[k] = m
        print(f"Число {moved} переміщено")

    elif n - 4 == k:
        m = board[n]
        board[n] = board[k]
        board[k] = m
        print(f"Число {moved} переміщено")

    elif n + 4 == k:
        m = board[n]
        board[n] = board[k]
        board[k] = m
        print(f"Число {moved} переміщено")

    else:
        print("Це число перемістити не можна")

    for i in board:
        print(i, end="\t")
        a += 1
        if a == 4:
            print()
            print("_______________")
            a = 0
    return board


def answer():
    while True:
        moved = int(input("Number to move >>"))
        if 1 <= moved <= 15:
            return moved
        else:
            print("Введіть число від 1 до 15")


print_greeting()
board = print_bord()
bord = initialize_bord()
while check(board):
    try_move = answer()
    move(board, try_move)
    print()

print("Congratulation You have orderedthe bord")
