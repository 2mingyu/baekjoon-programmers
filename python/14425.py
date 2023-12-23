"""
문자열 집합
"""
N, M = map(int, input().split())
S = set()
r = 0
for _ in range(N): S.add(input())
for _ in range(M): r += input() in S
print(r)