"""
랜선 자르기
"""
K, N = map(int, input().split())
c = [int(input()) for _ in range(K)]
l = 1
h = max(c)
m = (l+h) // 2
n = 0
while True:
    if h < l: break
    m = (l+h)//2
    n = 0
    for i in c: n += i // m
    if n >= N:
        r = m
        l = m+1
    else: h = m-1
print(r)