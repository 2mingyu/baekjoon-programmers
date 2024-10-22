"""
일우는 야바위꾼

INU 코드페스티벌 2020 A
"""
import sys
input = sys.stdin.readline

N, X, K = map(int, input().split())
for _ in range(K):
    A, B = map(int, input().split())
    if A == X: X = B
    elif B == X: X = A
print(X)