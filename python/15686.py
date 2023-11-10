"""
치킨 배달
"""
import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
house = []
chicken = []
for r in range(N):
    tmp = input().split()
    for c in range(N):
        if tmp[c] == '1': house.append((r, c))
        elif tmp[c] == '2': chicken.append((r, c))

result = float('INF')
for c in combinations(chicken, M):
    chicken_len_city = 0
    for h in house:
        chicken_len_house = float('INF')
        for cc in c:
            chicken_len_house = min(chicken_len_house, abs(h[0]-cc[0])+abs(h[1]-cc[1]))
        chicken_len_city += chicken_len_house
    result = min(result, chicken_len_city)
print(result)