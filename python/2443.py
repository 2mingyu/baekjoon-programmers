"""
별 찍기 - 6
"""
N = int(input())
for i in range(1, N+1):
    print(' '* (i-1), end="")
    print('*' * (2*(N-i)+1))