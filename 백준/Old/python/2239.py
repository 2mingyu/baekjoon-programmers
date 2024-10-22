"""
스도쿠

2580
"""
board = [list(map(int, input())) for _ in range(9)]
l = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            l.append((i, j))

def row(y, n):
    for i in range(9):
        if board[y][i] == n:
            return False
    return True

def column(x, n):
    for i in range(9):
        if board[i][x] == n:
            return False
    return True

def square(y, x, n):
    y = y - y%3
    x = x - x%3
    for i in range(y, y+3):
        for j in range(x, x+3):
            if board[i][j] == n:
                return False
    return True

def fill(n):
    if n == len(l):
        for b in board:
            for bb in b:
                print(bb, end='')
            print()
        exit(0)
    for i in range(1, 10):
        y, x = l[n]
        if row(y, i) and column(x, i) and square(y, x, i):
            board[y][x] = i
            fill(n+1)
            board[y][x] = 0

fill(0)