"""
상어 키우기

INU 코드페스티벌 2023 D번
"""
import sys
input = sys.stdin.readline
from collections import deque

N, K, T = map(int, input().split())
A = deque(sorted(list(map(int, input().split()))))
B = deque()
while A:
    a = A.popleft()
    if a >= T:
        A.appendleft(a)
        if B:
            T += B.pop()
            K -= 1
            if K == 0:
                break
        else:
            break
    else:
        B.append(a)
while B and K > 0:
    T += B.pop()
    K -= 1
print(T)