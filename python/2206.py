"""
벽 부수고 이동하기

(0,0) 에서 (N-1, M-1) 로 이동
벽 부순 여부에 따라 visited를 경우를 나눌 것..
visited를 3차원으로 ..
"""
import sys
from collections import deque

N, M = map(int, input().split())
m = []
for _ in range(N): m.append(sys.stdin.readline().strip())

def bfs():
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
    q = deque()
    visited[0][0] = [1, 1]
    q.append((0, 0, False, 1))
    while q:
        y, x, used_break, length = q.popleft()
        if y == N-1 and x == M-1: return length
        for dy, dx in [[0,1], [0,-1], [1,0], [-1,0]]:
            ny, nx = y+dy, x+dx
            if -1 < ny < N and -1 < nx < M and not visited[ny][nx][used_break]:
                if m[ny][nx] == '1':
                    if not used_break:
                        visited[ny][nx][1] = True
                        q.append((ny, nx, True, length+1))
                else:
                    visited[ny][nx][used_break] = True
                    q.append((ny, nx, used_break, length+1))
    return -1

print(bfs())