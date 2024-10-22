"""
No Brainer
"""
n = int(input())
for _ in range(n):
    X, Y = map(int, input().split())
    if X >= Y:
        print('MMM BRAINS')
    else:
        print('NO BRAINS')