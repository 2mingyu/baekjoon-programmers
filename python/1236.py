"""
성 지키기
"""
N, M = map(int, input().split())
l = [1] * M
t = 0
for _ in range(N):
    s = input()
    for i in range(M):
        if s[i] == 'X':
            l[i] = 0
    if 'X' not in s:
        t += 1
print(max(sum(l), t))