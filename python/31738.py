"""
매우 어려운 문제
N M
2 2 0
3 2 0
3 3 0
if N >= M: r = 0
N M
2 3 1
3 4 2
3 5 1
3 6 0
3 7 6
3 8 6
3 9 6
if N! < M: r = N
N M
5 5 0
5 6 0
5 7 1
5 8 0
5 9 3
5 10 0
5 11 10
5 12 0
5 13 3
5 14 8
5 15 0
5 16 8
"""
N, M = map(int, input().split())
if N >= M: print(0)
else:
    r = 1
    for i in range(1, N+1):
        r = r * i % M
    print(r)