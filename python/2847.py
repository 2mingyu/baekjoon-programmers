"""
게임을 만든 동준이
"""
N = int(input())
l = [int(input()) for _ in range(N)]
r = 0
for i in range(N-1, 0, -1):
    while l[i] <= l[i-1]:
        r += 1
        l[i-1] -= 1
print(r)