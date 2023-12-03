"""
드럼

INU 코드페스티벌 2023 B번
"""
import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
r = ''
for Z in range(1, X*Y+1):
    if Z % X == 0:
        if Z % Y == 0:
            r += '3'
        else:
            r += '2'
    elif Z % Y == 0:
        r += '1'
print(r)