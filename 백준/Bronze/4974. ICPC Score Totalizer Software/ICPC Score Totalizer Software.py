while True:
    n = int(input())
    if n == 0: break
    l = sorted(int(input()) for _ in range(n))
    t = l[1:-1]
    print(sum(t) // len(t))