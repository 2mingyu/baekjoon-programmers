"""
Fly me to the Alpha Centauri
1 = 1
2 = 1 1
3 = 1 1 1
4 = 1 2 1
5 = 1 2 1 1 or 1 1 2 1
6 = 1 2 2 1
7 = 1 2 2 1 1 or 1 1 2 2 1 or 1 2 1 2 1
8 = 1 2 2 2 1
9 = 1 2 3 2 1

z 1 2 3 4 5 6 7 8 9
r 1 2 3 3 4 4 5 5 5 6 6 6 7 7 7 7 8 8 8 8 (9*5) (10*5) (11*6) (12*6)
"""
T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    z = y-x
    n = 0
    while True:
        if z <= n*(n+1):
            break
        n += 1

    if z <= n**2:
        print(n*2 - 1)
    else:
        print(n*2)