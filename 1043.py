"""
거짓말

이게 시간복잡도가 안넘어가네
"""
N, M = map(int, input().split())
v = set(input().split()[1:])
p_list = []
for _ in range(M):
    p_list.append(set(input().split()[1:]))
for _ in range(M):
    for p in p_list:
        if p & v:
            v = v.union(p)
r = 0
for p in p_list:
    if not p & v:
        r += 1

print(r)