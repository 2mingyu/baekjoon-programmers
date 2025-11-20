T = int(input())
for _ in range(T):
    N, M, L = map(int, input().split())
    S = list(map(int, input().split()))
    for i in range(N):
        if S[i] > -1:
            L = max(L, M-S[i])
    s = ['s', ''][L == 1]
    print(f'The scoreboard has been frozen with {L} minute{s} remaining.')