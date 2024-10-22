"""
알파벳

231118 재채점 시간초과 다시풀이
"""
R, C = map(int, input().split())
board = []
for _ in range(R): board.append(input())
result = 0
visited = [0] * 26

def dfs(y, x, log):
    global result
    result = max(result, log)
    visited[ord(board[y][x])-65] = 1
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ny, nx = y+dy, x+dx
        if 0 <= ny < R and 0 <= nx < C:
            if not visited[ord(board[ny][nx])-65]:
                dfs(ny, nx, log+1)
                visited[ord(board[ny][nx])-65] = 0

dfs(0, 0, 1)
print(result)