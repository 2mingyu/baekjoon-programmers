N = int(input())
M = [input() for _ in range(N)]
K = int(input())
if K == 1:
    for e in M: print(e)
elif K == 2:
    for e in M: print(e[::-1])
else:
    for i in range(N): print(M[N-1-i])