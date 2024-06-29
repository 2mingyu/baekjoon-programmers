"""
진주로 가자! (Easy)
"""
N = int(input())
l = [0] * 1001
t = 0
for _ in range(N):
    D, C = input().split()
    if D == 'jinju': f = int(C)
    l[int(C)] += 1
print(f)
print(sum(l[f+1:]))