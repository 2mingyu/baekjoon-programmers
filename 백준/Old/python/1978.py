"""
소수 찾기
"""
input()
primeNumber = [False] * 2 + [True] * 999
for n in range(2, 1001):
    nn = n * 2
    while nn < 1001:
        primeNumber[nn] = False
        nn += n
r = 0
for i in list(map(int, input().split())):
    if primeNumber[i]: r += 1
print(r)