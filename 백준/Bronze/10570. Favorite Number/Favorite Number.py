N = int(input())
for _ in range(N):
    l = [0]*1001
    V = int(input())
    for _ in range(V):
        S = int(input())
        l[S] += 1
    m = 0
    for i in range(1, 1001):
        if l[i] > l[m]:
            m = i
    print(m)