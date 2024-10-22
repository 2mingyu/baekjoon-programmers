"""
공유기 설치
"""
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
X = sorted([int(input()) for _ in range(N)])
s, e = 1, X[-1] - X[0]
r = 0
while s <= e:
    count = 1
    m = (s+e) // 2
    now = X[0]
    for i in range(N):
        if X[i] - now >= m:
            count += 1
            now = X[i]

    if count >= C:
        r = max(r, m)
        s = m+1
    else:
        e = m-1
print(r)