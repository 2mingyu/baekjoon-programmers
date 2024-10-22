"""
쉽게 푸는 문제
"""
l = []
i = j = 1
for _ in range(1001):
    if j == 0:
        i += 1
        j = i
    l.append(i)
    j -= 1

A, B = map(int, input().split())
print(sum(l[A-1:B]))