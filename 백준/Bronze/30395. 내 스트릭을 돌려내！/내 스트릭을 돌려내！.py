N = int(input())
P = list(map(int, input().split()))
buy = [False] * (N + 2)
buy[0] = True  # 시작 시 장착

freeze = False
streak = 0
r = 0

for i in range(N):
    if buy[i]:
        freeze = True
    if P[i] > 0:
        streak += 1
    elif freeze:
        freeze = False
        if i + 2 < N:
            buy[i + 2] = True
    else:
        streak = 0
    r = max(r, streak)

print(r)