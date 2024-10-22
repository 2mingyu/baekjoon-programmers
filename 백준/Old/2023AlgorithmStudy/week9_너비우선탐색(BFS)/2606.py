"""
바이러스
"""
def check(c):
    checked[c] = True
    for j in l[c]:
        if not checked[j]:
            checked[j] = True
            check(j)

N = int(input())
M = int(input())
l = [[] for _ in range(N+1)]
checked = [False for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    l[a].append(b)
    l[b].append(a)
checked[1] = True
for i in l[1]:
    if not checked[i]:
        check(i)
print(sum(checked)-1)