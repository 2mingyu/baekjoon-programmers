"""
이진수
"""
T = int(input())
for _ in range(T):
    n = int(input())
    b = bin(n)[::-1]
    l = []
    for i in range(len(b)):
        if b[i] == '1': l.append(i)
    print(*l)