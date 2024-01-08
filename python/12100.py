"""
2048 (Easy)

반례모음
https://forward-gradually.tistory.com/83
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import deque

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
r = 0

def f(B, c, s):
    global r
    # print(s)
    # for b in B: print(b)
    if c == 5:
        for b in B: r = max(r, max(b))
        return
    # 왼쪽으로 밀기
    nA = [[0]*N for _ in range(N)]
    for i in range(N):
        q = deque([0])
        merged = False
        for j in range(N):
            if B[i][j]:
                if merged:
                    q.append(B[i][j])
                    merged = False
                else:
                    if q[-1] == B[i][j]:
                        q[-1] += B[i][j]
                        merged = True
                    else:
                        q.append(B[i][j])
        q.popleft()
        k = 0
        while q:
            nA[i][k] = q.popleft()
            k += 1
    f(nA, c+1, s+'왼')
    # 오른쪽으로 밀기
    nA = [[0]*N for _ in range(N)]
    for i in range(N):
        q = deque([0])
        merged = False
        for j in range(N-1, -1, -1):
            if B[i][j]:
                if merged:
                    q.append(B[i][j])
                    merged = False
                else:
                    if q[-1] == B[i][j]:
                        q[-1] += B[i][j]
                        merged = True
                    else:
                        q.append(B[i][j])
        q.popleft()
        k = -1
        while q:
            nA[i][k] = q.popleft()
            k -= 1
    f(nA, c+1, s+'오')
    # 위쪽으로 밀기
    nA = [[0]*N for _ in range(N)]
    for i in range(N):
        q = deque([0])
        merged = False
        for j in range(N):
            if B[j][i]:
                if merged:
                    q.append(B[j][i])
                    merged = False
                else:
                    if q[-1] == B[j][i]:
                        q[-1] += B[j][i]
                        merged = True
                    else:
                        q.append(B[j][i])
        q.popleft()
        k = 0
        while q:
            nA[k][i] = q.popleft()
            k += 1
    f(nA, c+1, s+'위')
    # 아래쪽으로 밀기
    nA = [[0]*N for _ in range(N)]
    for i in range(N):
        q = deque([0])
        merged = False
        for j in range(N-1, -1, -1):
            if B[j][i]:
                if merged:
                    q.append(B[j][i])
                    merged = False
                else:
                    if q[-1] == B[j][i]:
                        q[-1] += B[j][i]
                        merged = True
                    else:
                        q.append(B[j][i])
        q.popleft()
        k = -1
        while q:
            nA[k][i] = q.popleft()
            k -= 1
    f(nA, c+1, s+'아')

f(A, 0, '')
print(r)