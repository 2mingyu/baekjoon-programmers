"""
틱! 택! 토!
"""
a = int(input())
if a == 1: b = 2
else: b = 1
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(9):
    y, x = map(int, input().split())
    y -= 1
    x -= 1
    if i % 2: board[y][x] = b
    else: board[y][x] = a

    for y in range(3):
        if board[y][0] == board[y][1] == board[y][2] and board[y][0]:
            print(board[y][0])
            exit()
    for x in range(3):
        if board[0][x] == board[1][x] == board[2][x] and board[0][x]:
            print(board[0][x])
            exit()
    if board[0][0] == board[1][1] == board[2][2] and board[0][0]:
        print(board[0][0])
        exit()
    if board[0][2] == board[1][1] == board[2][0] and board[0][2]:
        print(board[0][2])
        exit()
print(0)