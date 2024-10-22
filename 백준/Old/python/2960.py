"""
에라토스테네스의 체
"""
N, K = map(int, input().split())
l = [1, 1] + [0 for _ in range(N-1)]
for i in range(N+1):
    if not l[i]:
        l[i] = 1
        K -= 1
        if K == 0: print(i); exit()
        t = i + i
        while t < N+1:
            if not l[t]:
                l[t] = 1
                K -= 1
                if K == 0: print(t); exit()
            t += i