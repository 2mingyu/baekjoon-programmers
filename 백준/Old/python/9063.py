"""
대지
"""
N = int(input())
xmin = ymin = 10000
xmax = ymax = -10000
for _ in range(N):
    x, y = map(int, input().split())
    xmin = min(x, xmin)
    xmax = max(x, xmax)
    ymin = min(y, ymin)
    ymax = max(y, ymax)
print((xmax-xmin)*(ymax-ymin))