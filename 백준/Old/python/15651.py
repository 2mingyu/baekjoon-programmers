"""
N과 M (3)
"""
def f(s, m):
    if not m: print(s)
    else:
        for i in range(1, N+1):
            f(s+str(i)+' ', m-1)

N, M = map(int, input().split())
for i in range(1, N+1):
    f(str(i)+' ', M-1)