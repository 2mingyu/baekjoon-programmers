"""
홀수
"""
l = []
for _ in range(7):
    a = int(input())
    if a % 2:
        l.append(a)
if l:
    print(sum(l))
    print(min(l))
else:
    print(-1)