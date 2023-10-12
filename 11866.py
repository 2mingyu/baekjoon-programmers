"""
요세푸스 문제 0
"""
N, K = map(int, input().split())
l = [(i+1) for i in range(N)]
p = []
i = 0
while l:
    i += K-1
    while i >= len(l): i -= len(l)
    p.append(l.pop(i))
print("<"+str(p)[1:-1]+">")