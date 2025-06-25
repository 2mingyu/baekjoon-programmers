while True:
    N = int(input())
    if not N: break
    l = [0]*49
    for _ in range(N):
        for i in list(map(int, input().split())): l[i-1] = 1
    print('Yes' if sum(l) == 49 else 'No')