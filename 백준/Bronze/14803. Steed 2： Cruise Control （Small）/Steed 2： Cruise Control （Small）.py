T = int(input())
for x in range(T):
    d, n = map(int, input().split())
    m = 0
    for _ in range(n):
        k, s = map(int, input().split())
        m = max(m, (d - k) / s)
    print(f"Case #{x+1}: {d / m:.6f}")