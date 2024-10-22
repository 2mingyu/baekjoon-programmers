"""
Claustrophobic Cows
"""
N = int(input())
l = [list(map(int, input().split()))for _ in range(N)]
m = float('inf')

for i in range(N):
    for j in range(i+1, N):
        d = abs(l[i][0] - l[j][0])**2 + abs(l[i][1] - l[j][1])**2
        if d < m:
            a, b, m = i, j, d
print(*sorted([a+1, b+1]))