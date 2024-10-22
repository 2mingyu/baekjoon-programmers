"""
N과 M (8)

L을 int로 안받고 문자열인 상태로 sort 하면 틀림
"""
def f(i):
    if len(s) == M:
        print(*s)
        return
    for j in range(i, N):
        s.append(L[j])
        f(j)
        s.pop()

N, M = map(int, input().split())
L = sorted(list(map(int, input().split())))
s = []
f(0)