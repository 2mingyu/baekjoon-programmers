"""
가운데를 말해요
"""
import sys
input = sys.stdin.readline
import heapq

N = int(input())
left, right = [], []
for _ in range(N):
    a = int(input())
    if len(left) == len(right):
        heapq.heappush(left, (-a, a))
    else:
        heapq.heappush(right, (a, a))
    if right and left[0][1] > right[0][0]:
        b = heapq.heappop(right)[0]
        c = heapq.heappop(left)[1]
        heapq.heappush(left, (-b, b))
        heapq.heappush(right, (c, c))
    print(left[0][1])