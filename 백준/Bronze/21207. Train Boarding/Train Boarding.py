N, L, P = map(int, input().split())
doors = [(i - 1) * L + L // 2 for i in range(1, N + 1)]
max_walk = 0
cnt = [0] * N
for _ in range(P):
    x = int(input())
    best_car, best_dist = 0, float('inf')
    for i, d in enumerate(doors):
        dist = abs(x - d)
        if dist <= best_dist:
            best_dist = dist
            best_car = i
    max_walk = max(max_walk, best_dist)
    cnt[best_car] += 1
print(max_walk)
print(max(cnt))