K = int(input())
for x in range(1, K+1):
    m, n = map(int, input().split())
    density = [0] + [int(input()) for _ in range(m)]
    s = 0
    for _ in range(n):
        h, w, d, i = map(int, input().split())
        s += h*w*d*density[i]
    print(f"Data Set {x}:\n{s}")