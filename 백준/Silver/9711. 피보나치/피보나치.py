T = int(input())
f = [1, 1]
for _ in range(10000):
    f.append(f[-1]+f[-2])
for x in range(T):
    P, Q = map(int, input().split())
    print(f"Case #{x+1}: {f[P-1] % Q}")