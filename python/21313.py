"""
문어
"""
N = int(input())
l = []
for _ in range(N//2 + 1):
    l.append(1)
    l.append(2)
if N%2:
    print(*l[:N-1]+[3])
else:
    print(*(l[:N]))