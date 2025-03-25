import sys
input = sys.stdin.readline

T = int(input())
for x in range(1, T+1):
    N, X = map(int, input().split())
    S = sorted(list(map(int, input().split())), reverse=True)
    V = [0] * N
    y = 0
    for i in range(N):
        if not V[i]:
            j = i+1
            while j < N:
                if not V[j] and S[i] + S[j] <= X:
                    V[j] = 1
                    break
                j += 1
            V[i] = 1
            y += 1
    print(f"Case #{x}: {y}")