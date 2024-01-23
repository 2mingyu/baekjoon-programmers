"""
텀 프로젝트
"""
import sys
sys.setrecursionlimit(10**6)

def dfs(j):
    global r

    visited[j] = 1
    tmp.append(j)
    if visited[s[j]]:
        for k in range(len(tmp)):
            if s[j] == tmp[k]:
                r -= len(tmp) - k
                break
    else:
        dfs(s[j])




T = int(input())
for _ in range(T):
    n = int(input())
    s = [0] + list(map(int, input().split()))
    visited = [0] * (n+1)
    r = n
    for i in range(1, n+1):
        if not visited[i]:
            tmp = []
            dfs(i)
    print(r)