"""
집합의 표현

union find 써야되는건 알겠는데 구현 헷갈리네
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if s[x] != x:
        s[x] = find(s[x])
    return s[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        s[y] = x
    else:
        s[x] = y

n, m = map(int, input().split())
s = [i for i in range(n+1)]
for _ in range(m):
    c, a, b = map(int, input().split())
    if a == b:
        if c == 1:
            print("YES")
        continue
    if a > b:
        a, b = b, a
    if c == 0:
        union(a, b)
    elif c == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")