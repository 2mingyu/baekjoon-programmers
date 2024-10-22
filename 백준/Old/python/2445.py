"""
별 찍기 - 8
"""
N = int(input())
for i in range(1, N+1):
    print('*'*i, end="")
    print(' '*(2*(N-i)), end="")
    print('*'*i)
for i in range(N-1, 0, -1):
    print('*'*i, end="")
    print(' '*(2*(N-i)), end="")
    print('*'*i)