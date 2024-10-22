"""
다리 놓기
조합 M C N ?
"""
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    r = 1
    for i in range(1, N+1):
        r = r * (M-i+1) / i
    print(int(r))