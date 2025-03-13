class Dice:
    def __init__(self, x, y, N, M, board):
        self.top = 0
        self.east = 0
        self.north = 0
        self.south = 0
        self.west = 0
        self.bottom = 0
        self.x = x
        self.y = y
        self.N = N
        self.M = M
        self.board = board

    def move(self, d):
        nx, ny = self.x, self.y
        if d == 1:
            ny += 1
        elif d == 2:
            ny -= 1
        elif d == 3:
            nx -= 1
        elif d == 4:
            nx += 1

        if not (0 <= nx < self.N and 0 <= ny < self.M):
            return

        self.x, self.y = nx, ny

        if d == 1:
            self.top, self.east, self.bottom, self.west = (
                self.west, self.top, self.east, self.bottom)
        elif d == 2:
            self.top, self.east, self.bottom, self.west = (
                self.east, self.bottom, self.west, self.top)
        elif d == 3:
            self.top, self.north, self.bottom, self.south = (
                self.south, self.top, self.north, self.bottom)
        elif d == 4:
            self.top, self.north, self.bottom, self.south = (
                self.north, self.bottom, self.south, self.top)

        if self.board[self.x][self.y] == 0:
            self.board[self.x][self.y] = self.bottom
        else:
            self.bottom = self.board[self.x][self.y]
            self.board[self.x][self.y] = 0

        print(self.top)


N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cl = list(map(int, input().split()))

dice = Dice(x, y, N, M, board)
for c in cl:
    dice.move(c)
