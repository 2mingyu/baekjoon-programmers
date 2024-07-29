"""
다음 소수
"""
import math

def p(x):
    if x < 2: return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0: return False
    return True

for _ in range(int(input())):
    n = int(input())
    while True:
        if p(n): print(n); break
        else: n += 1