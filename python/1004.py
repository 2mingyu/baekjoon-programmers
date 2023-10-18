"""
어린 왕자
출발점만 들어있는 행성계 수 + 도착점만 들어있는 행성계 수
"""
T = int(input())
for _ in range(T):
    a = 0
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        f1 = (cx-x1)**2 + (cy-y1)**2 < r**2
        f2 = (cx-x2)**2 + (cy-y2)**2 < r**2
        if f1 != f2: a += 1
    print(a)