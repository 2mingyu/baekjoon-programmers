"""
웰컴 키트
"""
N = int(input())
t = list(map(int, input().split()))
T, P = map(int, input().split())
a = 0
for s in t: a += s//T + bool(s%T)
print(a)
print(N//P, N%P)