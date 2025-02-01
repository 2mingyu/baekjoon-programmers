N = int(input())
S = 0
for _ in range(N):
    C, K = map(int, input().split())
    S += C*K
print(S)