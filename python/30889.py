"""
좌석 배치도

INU 코드페스티벌 2023 A번
"""
import sys
input = sys.stdin.readline

N = int(input())
s = [['.'] * 20 for _ in range(10)]
for _ in range(N):
    i = input()
    y = ord(i[0]) - 65
    x = int(i[1:]) - 1
    s[y][x] = 'o'
for y in range(10):
    for x in range(20):
        print(s[y][x], end='')
    print()