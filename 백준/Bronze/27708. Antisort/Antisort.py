T = int(input())
print(T)
for _ in range(T):
    input()
    print()
    N = int(input())
    print(N)
    S = sorted(list(map(int, input().split())))
    print(*S[1:]+[S[0]])