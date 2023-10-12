"""
나무 자르기
"""
N, M = map(int, input().split())
T = sorted(list(map(int, input().split())), reverse=True)
r, h = 1, T[0]
result = 0
g = 0
while r <= h:
    m = (r+h) // 2
    g = 0
    for t in T:
        if t > m:
            g += t-m
        else:
            break
    if g >= M:
        result = max(m, result)
        r = m + 1
    else: h = m - 1
print(result)