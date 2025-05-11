N = int(input())
R = 0
for _ in range(N):
    A, B, C = map(int, input().split())
    if A == B == C:
        T = 10000 + A*1000
    elif A == B or A == C:
        T = 1000 + A*100
    elif B == C:
        T = 1000 + B*100
    else:
        T = max(A, B, C)*100
    R = max(R, T)
print(R)