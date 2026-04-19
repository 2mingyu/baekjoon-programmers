N = int(input())
for _ in range(N):
    w = input().split()
    print(*w[2:], *w[:2])