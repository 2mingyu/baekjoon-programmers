K = int(input())
for x in range(K):
    y = 0
    n, s, d = map(int, input().split())
    for _ in range(n):
        di, vi = map(int, input().split())
        if di <= s*d:
            y += vi
    print(f'Data Set {x+1}:')
    print(y)
    print()