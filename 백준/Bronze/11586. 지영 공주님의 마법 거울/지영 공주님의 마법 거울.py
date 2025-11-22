N = int(input())
M = [input() for _ in range(N)]
K = int(input())
if K == 1:
    for e in M: print(e)
elif K == 2:
    for e in M: print(e[::-1])
else:
    for e in M[::-1]: print(e)