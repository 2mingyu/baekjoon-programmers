"""
수열의 합
"""
N, L = map(int, input().split())
for l in range(L, 101):
    tmp = l * (l - 1) // 2
    if N - tmp < 0:
        continue
    if (N - tmp) % l != 0:
        continue
    x = (N - tmp) // l
    if x < 0:
        continue
    print(*[x + i for i in range(l)])
    exit()
print(-1)
