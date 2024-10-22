"""
터렛
내접을 생각 못해서 틀렸었음
"""
import sys
import math

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    tmp = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if tmp == 0:    # 중심 같음
        if r1 == r2: print(-1)  # 반지름 같음
        else : print(0) # 반지름 다름
    elif tmp == r1 + r2: print(1)   # 외접
    elif tmp == abs(r2 - r1): print(1)  # 내접
    elif abs(r2 - r1) < tmp < r1 + r2: print(2)
    else: print(0)