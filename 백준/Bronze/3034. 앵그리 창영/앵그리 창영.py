N, W, H = map(int, input().split())
for _ in range(N):print(['NE', 'DA'][int(input())**2 <= W**2 + H**2])