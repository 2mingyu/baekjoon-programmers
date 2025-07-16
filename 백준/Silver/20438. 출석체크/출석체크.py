import sys
input = sys.stdin.readline

N, K, Q, M = map(int, input().split())
n = [False]*(N+3)
k = [False]*(N+3)
for e in list(map(int, input().split())):
    k[e] = True
for e in list(map(int, input().split())):
    if k[e]: continue
    i = e
    while i < N+3:
        if not k[i]:
            n[i] = True
        i += e
l = [0, 0, 0]
for e in n[3:]:
    if not e: l.append(l[-1]+1)
    else: l.append(l[-1])
for _ in range(M):
    S, E = map(int, input().split())
    print(l[E]-l[S-1])