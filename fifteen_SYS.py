import sys
def print_greeting():
    print("*" * 5, "Hello", "*" * 5)


def size():
    size = 0
    if len(sys.argv) != 2:
        print("Введіть розмір поля")
        exit(1)

    else:
        while size == 0:

            if not sys.argv[1].isdigit():
                print("Введіть розмір від 3 до 9")
                exit(1)
            if sys.argv[1].isdigit():
                if 3 > int(sys.argv[1]) or int(sys.argv[1]) > 9:
                    print("Введіть розмір від 3 до 9")
                    exit(2)
                else:
                    size = int(sys.argv[1])
    return size


def initialize_bord(size):
    """

    :return: list --> [15,14, ...., 3,1,2,0]

    """
    board = []
    for item in range(3, size ** 2):
        board.append(item)

    board = board[::-1]
    board.append(1)
    board.append(2)
    board.append("_")

    return board


def check(board):
    """

    :param board:
    :param bord: [1, 2, 3,...., 14, 15, 0] --> False otherwise True
    :return: True -- bord is not sorted
            False -- bord is sorted
    """
    winlist = []
    for win in range(1, size ** 2):
        winlist.append(win)

    #winlist = winlist[::-1]
    winlist.append("_")

    if board == winlist:
        print("Ви виграли")
        return False
    return True


def print_bord(board, size):
    a = 0

    pass
    for i in board:
        print(i, end="\t")
        a += 1
        if a == size:
            print()
            a = 0

    return board


def move(board, moved, size, imp1, imp2):
    possition = board.index(moved)
    space = board.index("_")
    # a = 0
    b = possition in imp1
    c = possition in imp2

    if space - 1 == possition and not b:
        m = board[space]
        board[space] = board[possition]
        board[possition] = m
        print(f"Число {moved} переміщено")

    elif space + 1 == possition and not c:
        m = board[space]
        board[space] = board[possition]
        board[possition] = m
        print(f"Число {moved} переміщено")

    elif space - size == possition:
        m = board[space]
        board[space] = board[possition]
        board[possition] = m
        print(f"Число {moved} переміщено")

    elif space + size == possition:
        m = board[space]
        board[space] = board[possition]
        board[possition] = m
        print(f"Число {moved} переміщено")

    else:
        print("Це число перемістити не можна")

    return board


def impossible_move1(size):
    imp = []
    for k in range(1, size):
        imp.append(k * size - 1)

    return imp


def impossible_move2(size):
    impos = []
    for k in range(1, size):
        impos.append(k * size)

    return impos


def print_file(board, size):
    x = 0
    with open("fifteen.txt", "a") as f:
        for line in board:
            print(line, file=f, end="\t")
            x += 1
            if x == size:
                f.write("\n")
                x = 0
        f.write("__" * size * 2 + "\n")


def answer():
    while True:
        moved = int(input("Number to move >> "))
        if 1 <= moved <= size**2-1:
            return moved
        else:
            print(f"Введіть число від 1 до {size**2-1} ")


size = size()

print_greeting()

board = initialize_bord(size)

imp1 = impossible_move1(size)

imp2 = impossible_move2(size)

while check(board):
    print_bord(board, size)
    try_move = answer()
    move(board, try_move, size, imp1, imp2)
    print_file(board, size)
    print()

print("Congratulation You have ordered the bord")

