"""
구간 합 구하기
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
l = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    ll = [0] + list(map(int, input().split()))
    for j in range(1, N+1):
        l[i][j] = ll[j] + l[i-1][j] + l[i][j-1] - l[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(l[x2][y2] - l[x2][y1-1] - l[x1-1][y2] + l[x1-1][y1-1])