"""
키보드 이벤트
"""
N, M = map(int, input().split())
l = []
for _ in range(M):
    a, b, c = input().split()
    l.append([int(a), int(b), c])
for ll in sorted(sorted(l, key=lambda x: x[0]), key=lambda x: x[1]):
    print(ll[2], end="")