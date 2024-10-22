"""
민주주의
"""
N, M = map(int, input().split())
r = 0
for _ in range(N):
    s = input()
    if s.count('O') > M//2: r += 1
print(r)