"""
Race Results
"""
N = int(input())
l = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[0], x[1], x[2]))
for e in l: print(*e)