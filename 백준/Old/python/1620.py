"""
나는야 포켓몬 마스터 이다솜
"""
import sys
N, M = map(int, input().split())
d = dict()
l = ['']
for n in range(1, N+1):
    i = sys.stdin.readline().strip()
    d[i] = n
    l.append(i)
for _ in range(M):
    q = sys.stdin.readline().strip()
    try:
        q = int(q)
        print(l[q])
    except:
        print(d[q])