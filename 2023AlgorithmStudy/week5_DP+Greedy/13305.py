"""
가장 기름 싼 곳에서 기름 최대한 채우기
다음 도시로 가기 위한 비용 = 여태까지중 가장 싼 곳 * 거리
"""
import sys

N = int(input())
distances = list(map(int, sys.stdin.readline().strip().split()))
prices = list(map(int, sys.stdin.readline().strip().split()))
minPrice = 1000000000
totalPrice = 0
for i in range(N-1):
    minPrice = min(minPrice, prices[i])
    totalPrice += minPrice * distances[i]
print(totalPrice)