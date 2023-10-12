"""
좌표 정렬하기
"""
import sys
xy=[]
for _ in range(int(input())):xy.append(list(map(int,sys.stdin.readline().split())))
for x,y in sorted(xy):print(x,y)