"""
알파벳
"""
R, C = map(int, input().split())
board = []
for _ in range(R): board.append(input())
result = 0

def dfs(y, x, log):
    global result
    log += board[y][x]
    result = max(result, len(log))
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ny, nx = y+dy, x+dx
        if 0 <= ny < R and 0 <= nx < C:
            if board[ny][nx] not in log:
                dfs(ny, nx, log)

dfs(0, 0, "")
print(result)