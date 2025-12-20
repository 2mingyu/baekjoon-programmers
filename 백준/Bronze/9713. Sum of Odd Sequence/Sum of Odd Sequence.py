T = int(input())
for _ in range(T):
    N = int(input())
    t = 0
    for i in range(N+1):
        if i%2: t += i
    print(t)