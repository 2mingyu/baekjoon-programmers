"""
착신 전환 소동
"""
N = int(input())
a = [0] + list(map(int, input().split()))
r = 0
for i in range(1, N):
    if i == a[i]:
        a[i] += 1
        r += 1
if N == a[N]:
    a[N] -= 1
    r += 1
print(r)
print(*a[1:])