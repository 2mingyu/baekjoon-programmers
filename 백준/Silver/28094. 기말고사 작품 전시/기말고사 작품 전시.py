import sys
input = sys.stdin.readline

def dfs(s, v):
    global score
    global count
    if len(s) == N:
        tscore = 0
        for i in range(N-1):
            for j in range(i+1, N):
                tscore += V[s[i]][s[j]]
        if tscore > score:
            score = tscore
            count = 1
        elif tscore == score:
            count += 1
        return
    for i in range(1, N+1):
        if not v[i]:
            s.append(i)
            v[i] = 1
            dfs(s, v)
            s.pop()
            v[i] = 0


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    V = [[0]*(N+1) for _ in range(N+1)]
    for j in range(M):
        Vj, Aj, Bj = map(int, input().split())
        V[Aj][Bj] += Vj
    score = 0
    count = 0
    visited = [0]*(N+1)
    dfs([], visited)
    print(score, count)