"""
볶음밥 지키기

INU 코드페스티벌 2023 C번
"""
import sys
input = sys.stdin.readline

N, R = map(int, input().split())
RR = R**2
rice = []
r = [0, 0]
n = 0
for _ in range(N):
    x, y = map(int, input().split())
    rice.append([x,y])
for x in range(-100, 101):
    for y in range(-100, 101):
        tmp = 0
        for rice_x, rice_y in rice:
            if (x-rice_x)**2 + (y-rice_y)**2 <= RR:
                tmp += 1
        if tmp > n:
            n = tmp
            r = [x, y]

print(r[0], r[1])